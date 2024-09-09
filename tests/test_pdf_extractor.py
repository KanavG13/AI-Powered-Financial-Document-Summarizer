import unittest
from src.pdf_extractor import PDFExtractor

class TestPDFExtractor(unittest.TestCase):
    def test_extract_text(self):
        extractor = PDFExtractor('tests/Apple_10Q.pdf')
        text = extractor.extract_text()
        self.assertTrue(len(text) > 0)
        self.assertIn("UNITED STATES", text)  # Example assertion

if __name__ == '__main__':
    unittest.main()

