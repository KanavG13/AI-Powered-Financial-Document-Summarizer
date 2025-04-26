import unittest
from src.text_processor import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor()
    
    def test_preprocess_text(self):
        text = "This is a sample text.\nWith some new lines."
        lines = self.processor.preprocess_text(text)
        self.assertEqual(len(lines), 1)  # Expecting 1 line after preprocessing
    
    def test_format_text(self):
        lines = ["BUSINESS OVERVIEW", "Company: XYZ Corp"]
        formatted_text = self.processor.format_text(lines)
        self.assertIn("### BUSINESS OVERVIEW ###", formatted_text)
    
    def test_enhance_text_with_nlp(self):
        text = "This is a sentence. This is another sentence."
        enhanced_text = self.processor.enhance_text_with_nlp(text)
        self.assertIn("This is a sentence.", enhanced_text)
    
    def test_chunk_text(self):
        text = " ".join(["word"] * 10000)  # Long text
        chunks = self.processor.chunk_text(text, chunk_size=3000)
        self.assertEqual(len(chunks), 4)

if __name__ == '__main__':
    unittest.main()


