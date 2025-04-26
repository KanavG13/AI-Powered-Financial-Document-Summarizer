import logging
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize ChromaDB client with configuration
client = chromadb.Client(Settings(persist_directory=os.getenv("CHROMADB_PERSIST_DIRECTORY", "./chroma_db")))

# Create or get a collection for embeddings
def get_or_create_collection(name: str):
    try:
        logging.info(f"Getting or creating collection: {name}")
        return client.get_or_create_collection(name=name)
    except Exception as e:
        logging.error(f"Failed to get or create collection: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to get or create collection: {str(e)}")

# Add embeddings to the collection
def add_embeddings(collection, ids: list, embeddings: list, metadatas: list):
    try:
        logging.info(f"Adding embeddings to collection: {collection.name}")
        collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas)
    except Exception as e:
        logging.error(f"Failed to add embeddings: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to add embeddings: {str(e)}")

# Query embeddings from the collection
def query_embeddings(collection, query_embedding: list, top_k: int = 5):
    try:
        logging.info(f"Querying top {top_k} embeddings from collection: {collection.name}")
        return collection.query(query_embeddings=[query_embedding], n_results=top_k)
    except Exception as e:
        logging.error(f"Failed to query embeddings: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to query embeddings: {str(e)}")
