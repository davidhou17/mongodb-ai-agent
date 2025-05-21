# MongoDB-native AI agent

Demo AI agent using MongoDB, Voyage AI, and OpenAI that implements agentic RAG and agent memory. No agent-specific frameworks needed.

Tools: `vector_seach_tool` and `calculator_tool`

## About
Workflow:
- Chunk and ingest vector embeddings into MongoDB Atlas. Uses LangChain for loading/chunking.
- Specify the session id (agent will persist conversation interactions in a MongoDB collection).
- Run queries about sample data (recent MongoDB earnings report) or math operations to use tools.

Models used: 
- Voyage AI: `voyage-3-large`
- OpenAI: `gpt-4o`

Prompt engineering methods used:
- reAct + few-shot prompting

## Configuration

1. Run:
```
pip install --quiet --upgrade pymongo voyageai openai langchain langchain_mongodb langchain_community
```

2. Create `.env` file with necessary credentials (MongoDB Atlas connection string, Voyage AI, and OpenAI API keys)

3. Run `python main.py`
