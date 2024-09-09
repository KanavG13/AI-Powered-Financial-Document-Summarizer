import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.chromadb_dir = os.getenv("CHROMADB_PERSIST_DIRECTORY", "./chroma_db")
        self.num_clusters = int(os.getenv("NUM_CLUSTERS", 5))

    def get_openai_api_key(self):
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY not found in environment variables")
        return self.api_key

    def get_chromadb_directory(self):
        return self.chromadb_dir

    def get_num_clusters(self):
        return self.num_clusters
