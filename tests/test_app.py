import unittest
from src.pdf_extractor import PDFExtractor
from src.text_processor import TextProcessor
from src.openai_utils import generate_summary
from src.docx_utils import save_to_docx
from docx import Document
import os

class TestAppIntegration(unittest.TestCase):
    def setUp(self):
        self.pdf_path = 'tests/Apple_10Q.pdf'
        self.extractor = PDFExtractor(self.pdf_path)
        self.processor = TextProcessor()
    
    def test_full_workflow(self):
        # Extract text
        raw_text = self.extractor.extract_text()
        
        # Process text
        lines = self.processor.preprocess_text(raw_text)
        formatted_text = self.processor.format_text(lines)
        enhanced_text = self.processor.enhance_text_with_nlp(formatted_text)
        chunks = self.processor.chunk_text(enhanced_text)
        
        # Generate summary
        combined_text = " ".join(chunks)
        summary = generate_summary(combined_text, "Summarize this text")
        
        # Save summary
        output_path = 'tests/output.docx'
        save_to_docx(summary, output_path, "Test Summary")
        
        # Validate output
        self.assertTrue(os.path.exists(output_path))
        
        # Use python-docx to read the content
        doc = Document(output_path)
        doc_text = '\n'.join([para.text for para in doc.paragraphs])
        self.assertIn("Test Summary", doc_text)
        
        # Cleanup
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    unittest.main()