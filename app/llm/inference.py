import requests, sys
from app.core.config import get_settings

class OllamaClient:
    def generate(self, prompt:str)->str:
        settings = get_settings()
        response = requests.post(url=f"{settings.LLM_SRV_URL}/api/generate", json={
                                                                            'model':settings.LLM_MODEL_NAME,
                                                                            'prompt': prompt,
                                                                            'stream': False
                                                                            })
        response.raise_for_status()

        # print("Status Code:", response.status_code)
        # print("Response Text:", response.text)
        # sys.exit(0)
        print(response.json()['response'])
        return response.json()['response']
    
ollama_client = OllamaClient()