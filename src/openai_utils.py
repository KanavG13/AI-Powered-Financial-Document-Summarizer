import logging
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI API client with the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=api_key)

def generate_summary(text, template):
    try:
        logging.info("Generating summary")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior financial analyst with over 20 years of experience in evaluating company financials, including 10-K reports and financial analyst reports. Your goal is to create comprehensive and concise summaries that are insightful and actionable for financial advisors. Ensure that the summary adheres to the specified format and includes all key details."
                },
                {
                    "role": "user",
                    "content": f"{template}\n\n{text}"
                }
            ]
        )
        logging.info("Summary generated successfully")
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Failed to generate summary: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to generate summary: {str(e)}")

def generate_embeddings(text):
    try:
        logging.info("Generating embeddings")
        response = client.embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )
        logging.info("Embeddings generated successfully")
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Failed to generate embeddings: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to generate embeddings: {str(e)}")
