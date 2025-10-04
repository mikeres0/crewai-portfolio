# test_azure.py
from dotenv import load_dotenv
import os

load_dotenv()

print("Azure API Key:", os.getenv("AZURE_API_KEY")[:10] + "..." if os.getenv("AZURE_API_KEY") else "NOT SET")
print("Azure Base:", os.getenv("AZURE_API_BASE"))
print("Azure Version:", os.getenv("AZURE_API_VERSION"))
print("Deployment Name:", os.getenv("AZURE_DEPLOYMENT_NAME"))
print("OpenAI Key:", os.getenv("OPENAI_API_KEY", "NOT SET"))

from crewai import LLM

llm = LLM(
    model=os.getenv("AZURE_DEPLOYMENT_NAME"), 
    api_key=os.getenv("AZURE_API_KEY"),
    base_url=os.getenv("AZURE_API_BASE"),
    api_version=os.getenv("AZURE_API_VERSION", "2024-02-15-preview"),
)

print("LLM configured successfully!")
print("Testing connection...")
response = llm.call("Hello, this is a test")
print("Response:", response)