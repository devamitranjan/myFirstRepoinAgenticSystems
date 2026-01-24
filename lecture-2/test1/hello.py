from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
database_url = os.getenv("DATABASE_URL")
print(api_key)
print(database_url)