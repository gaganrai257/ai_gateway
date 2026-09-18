from ai_gateway.providers.base import LLMProvider
from ai_gateway.config import settings
from ai_gateway.schemas import ChatResponse, ChatRequest

import httpx




class GeminiAdapter(LLMProvider):

    def __init__(self):

        self.api_key = settings.GEMINI_API_KEY#taking key from the .env
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"


    async def generate_completion(self, request: ChatRequest)->ChatResponse:

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        payload = request.model_dump(exclude_none=True)

#using the httpx to send the chatrequest to the gemini with the other information for authorizationa dn stuff
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                headers = headers,
                json=payload,
                timeout=10.0
            )

            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                print("🚨 Gemini ERROR DETAILS 🚨")
                print(e.response.text)
                raise e
#response error handled from the gemini api

            return ChatResponse(**response.json())#this match the response dict to out pydantic schema



        
    