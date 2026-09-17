from ai_gateway.providers.base import LLMProvider
from ai_gateway.config import settings
from ai_gateway.schemas import ChatResponse, ChatRequest

import httpx




class GroqAdapter():

    def __init__(self):

        self.api_key = settings.GROQ_API_KEY#taking key from the .env
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"


    async def generate_completion(self, request: ChatRequest)->ChatResponse:

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        payload = request.model_dump(exclude_none=True)

#using the httpx to send the chatrequest to the groq with the other information for authorizationa dn stuff
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
                print("🚨 GROQ ERROR DETAILS 🚨")
                print(e.response.text)
                raise e
#response error handled from the groq api

            return ChatResponse(**response.json())#this match the response dict to out pydantic schema



        
    