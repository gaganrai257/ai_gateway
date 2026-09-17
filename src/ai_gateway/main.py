from fastapi import FastAPI
from ai_gateway.schemas import Message,Choice,ChatRequest,ChatResponse 
from ai_gateway.providers.groq import GroqAdapter
from ai_gateway.config import settings
print("====== STRICT SANITY CHECK ======")
raw_key = settings.GROQ_API_KEY

# This will print True if you accidentally copied a space
print(f"Starts with space? : {raw_key.startswith(' ')}")
print(f"Ends with space?   : {raw_key.endswith(' ')}")

# This reveals the exact raw string Python sees
print(f"Exact raw string   : {repr(raw_key)}")
print("=================================")



app = FastAPI(title="ai_gatway", version="0.1.0", description="Intelligent Router and API GATEWAY")
groq_adapter = GroqAdapter()
@app.post("/v1/chat/completion")
async def chat_completion(request: ChatRequest):
    print(f"Received the request for the model{request.model}")

    response = await groq_adapter.generate_completion(request)

    return response

