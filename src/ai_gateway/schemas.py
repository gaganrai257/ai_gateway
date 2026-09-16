from typing import Literal

from pydantic import BaseModel, Field

'''it is how the official json formt is for the message'''
class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=2)

class Choice(BaseModel):
    message: Message

'''It is the univeral way the user will send and talk to our gateway, and here according 
to the models they want to talk to we will use the adapters to translate it to that 
specific model json format '''
class ChatRequest(BaseModel):
    model : str
    messages: list[Message]
    temperature: float|None = Field(default=0.7, ge=0.0 , le=2.0)
    max_tokens: int|None = Field(default=200, ge=10, le=32000)
    stream: bool = Field(default=False)


'''There are also other response we can get from the opeai but
 for the the first we will go with this only and develop more'''
class ChatResponse(BaseModel):
    model: str
    choices: list[Choice]
    



