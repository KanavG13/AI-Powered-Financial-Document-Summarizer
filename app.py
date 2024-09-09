import logging
from src.logging_config import setup_logging
import streamlit as st
from src.config_manager import ConfigManager
from src.pdf_extractor import PDFExtractor
from src.text_processor import TextProcessor
from src.openai_utils import generate_summary, generate_embeddings
from src.docx_utils import save_to_docx
from src.chromadb_utils import get_or_create_collection, add_embeddings, query_embeddings
from src.templates import template_2_page, template_1_page
import numpy as np
from sklearn.cluster import KMeans
import os

# Setup logging
setup_logging()

# Initialize configuration manager
config = ConfigManager()

def validate_input_files(uploaded_files):
    if not uploaded_files:
        raise ValueError("No files uploaded. Please upload at least one PDF file.")
    for file in uploaded_files:
        if not file.name.endswith('.pdf'):
            raise ValueError(f"Invalid file type: {file.name}. Only PDF files are supported.")

def create_output_folder():
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Created output directory: {output_folder}")

def main():
    logging.info("Starting Financial Report Summarization application")
    
    st.title("Financial Report Summarization")
    
    uploaded_files = st.file_uploader("Upload PDF Files", type="pdf", accept_multiple_files=True)
    
    if st.button("Generate Summaries"):
        try:
            validate_input_files(uploaded_files)
            create_output_folder()  # Ensure the output folder exists
            
            with st.spinner("Generating summaries... This may take a few minutes."):
                combined_text = ""
                pdf_filenames = []
                
                for uploaded_file in uploaded_files:
                    logging.info(f"Processing file: {uploaded_file.name}")
                    pdf_bytes = uploaded_file.read()
                    pdf_path = f"temp_{uploaded_file.name}"
                    pdf_filenames.append(pdf_path)
                    
                    with open(pdf_path, 'wb') as f:
                        f.write(pdf_bytes)
                    
                    extractor = PDFExtractor(pdf_path)
                    raw_text = extractor.extract_text()
                    combined_text += raw_text + "\n"
                
                processor = TextProcessor()
                lines = processor.preprocess_text(combined_text)
                formatted_text = processor.format_text(lines)
                enhanced_text = processor.enhance_text_with_nlp(formatted_text)
                chunks = processor.chunk_text(enhanced_text, chunk_size=3000)
                
                if not chunks:
                    st.error("No valid text chunks generated from the provided PDFs.")
                    logging.error("No valid text chunks generated from the provided PDFs.")
                    return
                
                chunk_embeddings = [generate_embeddings(chunk) for chunk in chunks]
                
                collection_name = 'financial_report_embeddings'
                collection = get_or_create_collection(collection_name)
                
                ids = [f"chunk_{i}" for i in range(len(chunks))]
                metadatas = [{'text': chunk} for chunk in chunks]
                add_embeddings(collection, ids, chunk_embeddings, metadatas)
                
                # Adjust the number of clusters dynamically
                n_clusters = min(len(chunk_embeddings), config.get_num_clusters())
                if n_clusters < 1:
                    n_clusters = 1
                
                kmeans = KMeans(n_clusters=n_clusters, random_state=0)
                clusters = kmeans.fit_predict(chunk_embeddings)
                
                cluster_summaries = []
                for cluster_id in range(n_clusters):
                    cluster_text = " ".join([chunks[i] for i in range(len(chunks)) if clusters[i] == cluster_id])
                    cluster_summary = generate_summary(cluster_text, f"Summarize the financial reports for cluster {cluster_id + 1}:")
                    cluster_summaries.append(cluster_summary)
                
                combined_cluster_summaries = "\n".join(cluster_summaries)
                
                summary_2_page = generate_summary(combined_cluster_summaries, template_2_page)
                summary_1_page = generate_summary(summary_2_page, template_1_page)
                
                save_to_docx(summary_2_page, 'output/summary2page.docx', '2-Page Summary')
                save_to_docx(summary_1_page, 'output/summary1page.docx', '1-Page Summary')

                st.markdown("<h2 style='text-align: center; color: green;'>Both the summaries have been exported to your project's output folder</h2>", unsafe_allow_html=True)
                st.markdown("<h4>A preview of the summaries is shown below:</h4>", unsafe_allow_html=True)
                
                st.subheader("Generated 2-Page Summary:")
                st.write(summary_2_page)
                
                st.subheader("Generated 1-Page Summary:")
                st.write(summary_1_page)
                
                # Cleanup temporary files
                for filename in pdf_filenames:
                    if os.path.exists(filename):
                        os.remove(filename)
            
        except ValueError as ve:
            st.error(str(ve))
            logging.error(f"Validation error: {str(ve)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == '__main__':
    main()
