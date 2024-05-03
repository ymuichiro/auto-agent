from os import getenv
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_DEPLOYMENT_NAME: str = getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "")
AZURE_OPENAI_ENDPOINT: str = getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_KEY: str = getenv("AZURE_OPENAI_API_KEY", "")

print("AZURE_OPENAI_DEPLOYMENT_NAME:", AZURE_OPENAI_DEPLOYMENT_NAME)
