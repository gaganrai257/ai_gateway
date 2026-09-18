from fastapi import FastAPI
from ai_gateway.schemas import Message, Choice, ChatRequest, ChatResponse
from ai_gateway.providers.groq import GroqAdapter
from ai_gateway.providers.gemini import GeminiAdapter
from ai_gateway.config import settings


app = FastAPI(title="ai_gatway", version="0.1.0", description="Intelligent Router and API GATEWAY")

def resolve_provider(model: str):
    model_name = model.lower()
    if "gemini" in model_name:
        return GeminiAdapter
    if "groq" in model_name or "llama" in model_name or "openai" in model_name or "qwen" in model_name or "whispher" in model_name:
        return GroqAdapter
    raise ValueError(f"Unsupported model provider for: {model}")


@app.post("/v1/chat/completion")
async def chat_completion(request: ChatRequest):
    print(f"Received the request for the model {request.model}")

    provider_cls = resolve_provider(request.model)
    provider = provider_cls()
    response = await provider.generate_completion(request)

    return response

