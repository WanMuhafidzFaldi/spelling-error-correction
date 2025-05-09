import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        """
        Initialize the Ollama client.
        
        Args:
            base_url (str): The base URL for Ollama API
        """
        self.base_url = base_url
        self.api_endpoint = f"{self.base_url}/api/generate"
    
    def correct_spelling(self, text, model="llama3", system_prompt=None):
        """
        Send a text to Ollama for spelling correction.
        
        Args:
            text (str): The text containing spelling errors
            model (str): The model to use for generation
            system_prompt (str): Optional system prompt
            
        Returns:
            str: The corrected text from the model
        """
        if system_prompt is None:
            system_prompt = ("You are a helpful assistant that corrects spelling errors. "
                           "Your task is to fix any misspelled words in the text provided. "
                           "Only correct the spelling while maintaining the original meaning. "
                           "Do not add any explanations or extra text. "
                           "Just return the corrected sentence.")
        
        payload = {
            "model": model,
            "prompt": text,
            "system": system_prompt,
            "stream": False,
            "temperature": 0.1,  # Lower temperature for more deterministic results
        }
        
        try:
            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["response"].strip()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return None
