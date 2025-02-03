from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the GROQ_API_KEY
groq_api_key = os.getenv("GROQ_API_KEY")
print(f"GROQ_API_KEY: {groq_api_key}")  # Debugging: Print the key to verify