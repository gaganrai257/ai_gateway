from abc import ABC, abstractmethod

from ai_gateway.schemas import ChatRequest, ChatResponse


#abstract calss/contract every llmprovider inherits from this ,and will definitly provide the required function
class LLMProvider(ABC):

    @abstractmethod
    async def generate_completion(self, request: ChatRequest) -> ChatResponse :
        '''will take the standard chat form the gatway and 
        will translate it and send to the specific provider and 
        will give back us the response in standard way again'''
        pass
    


