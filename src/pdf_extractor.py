import logging
import pdfplumber
from typing import List

class PDFExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self) -> str:
        logging.info(f"Extracting text from PDF: {self.file_path}")
        try:
            with pdfplumber.open(self.file_path) as pdf:
                text = ''
                for page in pdf.pages:
                    page_text = self._extract_page_text(page)
                    if page_text:
                        text += page_text
            if not text:
                raise ValueError("No text found in PDF.")
            return text
        except Exception as e:
            logging.error(f"Failed to extract text from PDF: {str(e)}", exc_info=True)
            raise RuntimeError(f"Failed to extract text from PDF: {str(e)}")

    def _extract_page_text(self, page) -> str:
        page_text = page.extract_text()
        if not page_text:
            page_text = self._extract_text_from_tables(page)
        return page_text

    def _extract_text_from_tables(self, page) -> str:
        text = ''
        for table in page.extract_tables():
            for row in table:
                text += ' '.join([str(cell) for cell in row if cell]) + '\n'
        return text
