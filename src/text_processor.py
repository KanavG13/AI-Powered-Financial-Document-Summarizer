import logging
import re
import spacy
from spacy.cli import download

class TextProcessor:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            logging.info("Downloading en_core_web_sm model...")
            download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def preprocess_text(self, text):
        try:
            logging.info("Preprocessing text")
            if not text:
                raise ValueError("Empty text provided for preprocessing.")
            text = re.sub(r'\s+', ' ', text)
            lines = text.split("\n")
            logging.info("Text preprocessed successfully")
            return lines
        except Exception as e:
            logging.error(f"Failed to preprocess text: {str(e)}", exc_info=True)
            raise

    def format_text(self, lines):
        try:
            logging.info("Formatting text")
            if not lines:
                raise ValueError("Empty lines provided for formatting.")
            formatted_text = ""
            for line in lines:
                if re.match(r'^[A-Z\s]+$', line.strip()):
                    formatted_text += f"\n### {line.strip()} ###\n"
                elif re.match(r'^[A-Za-z\s]+:$', line.strip()):
                    formatted_text += f"\n**{line.strip()}**\n"
                else:
                    formatted_text += line.strip() + " "
            logging.info("Text formatted successfully")
            return formatted_text
        except Exception as e:
            logging.error(f"Failed to format text: {str(e)}", exc_info=True)
            raise

    def enhance_text_with_nlp(self, text):
        try:
            logging.info("Enhancing text with NLP")
            if not text:
                raise ValueError("Empty text provided for NLP enhancement.")
            doc = self.nlp(text)
            enhanced_text = ""
            for sent in doc.sents:
                enhanced_text += sent.text + "\n"
            logging.info("Text enhanced with NLP successfully")
            return enhanced_text
        except Exception as e:
            logging.error(f"Failed to enhance text with NLP: {str(e)}", exc_info=True)
            raise

    def chunk_text(self, text, chunk_size=3000):
        try:
            logging.info("Chunking text")
            if not text:
                raise ValueError("Empty text provided for chunking.")
            words = text.split()
            chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
            if not chunks:
                raise ValueError("No chunks created from the text.")
            logging.info("Text chunked successfully")
            return chunks
        except Exception as e:
            logging.error(f"Failed to chunk text: {str(e)}", exc_info=True)
            raise
