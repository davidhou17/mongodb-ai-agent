# MongoDB-native AI agent

Demo AI agent using MongoDB, Voyage AI, OpenAI, and LangChain that implements agentic RAG and agent memory. No agent frameworks needed.

Tools: vector_seach_tool and calculator_tool

Agent workflow:
- Chunk and ingest vector embeddings into MongoDB Atlas.
- Specify the session id (agent will persist conversation interactions in a MongoDB collection).
- Run queries about sample data (recent MongoDB earnings report) or math operations to use tools.

Models used: 
- Voyage AI: `voyage-3-large`
- OpenAI: `gpt-4o`

Prompt engineering methods used:
- reAct + few-shot prompting

## Dependencies

Run:
```
pip install --quiet --upgrade pymongo voyageai openai langchain langchain_mongodb langchain_community
```

