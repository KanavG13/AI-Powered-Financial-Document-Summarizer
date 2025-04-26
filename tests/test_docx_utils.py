import unittest
from docx import Document
import os
from src.docx_utils import save_to_docx

class TestDocxUtils(unittest.TestCase):
    def test_save_to_docx(self):
        text = "This is a test document."
        filepath = 'tests/test_output.docx'
        title = "Test Document"
        
        save_to_docx(text, filepath, title)
        
        # Check if file is created
        self.assertTrue(os.path.exists(filepath))
        
        # Open the document and verify content
        doc = Document(filepath)
        doc_text = '\n'.join([para.text for para in doc.paragraphs])
        self.assertIn("This is a test document.", doc_text)
        
        # Cleanup
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
