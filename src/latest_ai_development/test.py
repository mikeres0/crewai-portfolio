# Save as quick_test.py
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["AZURE_API_KEY"] = os.getenv("AZURE_API_KEY")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_API_BASE")
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION")

import litellm

base = os.getenv("AZURE_API_BASE").rstrip('/')
deployment = os.getenv("AZURE_DEPLOYMENT_NAME")

print(f"Testing: azure/{deployment}")
print(f"Base: {base}")

response = litellm.completion(
    model=f"azure/{deployment}",
    messages=[{"role": "user", "content": "Hi"}],
    api_key=os.getenv("AZURE_API_KEY"),
    api_base=base,
    api_version=os.getenv("AZURE_API_VERSION")
)

print(f"✅ Success: {response.choices[0].message.content}")