from pymongo import MongoClient
from openai import OpenAI
import voyageai
from dotenv import load_dotenv
import os

# Load environment variables once
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# MongoDB Atlas configuration
mongo_client = MongoClient(MONGODB_URI)
agent_db = mongo_client["ai_agent_db"]
vector_collection = agent_db["embeddings"]
memory_collection = agent_db["chat_history"]

# Model configuration
voyage_client = voyageai.Client()
openai_client = OpenAI()
VOYAGE_MODEL = "voyage-3-large"
OPENAI_MODEL = "gpt-4o"
