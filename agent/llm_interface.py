import openai
import requests
import anthropic
import yaml

# Charger les configurations depuis config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Charger les clés API et les autres paramètres depuis le fichier config.yaml
openai.api_key = config.get("openai_api_key")
anthropic_api_key = config.get("anthropic_api_key")
ollama_host = config.get("ollama_host")
ollama_model = config.get("ollama_model")

class LLMClient:
    def __init__(self, provider, model, api_key):
        self.provider = provider
        self.model = model
        self.api_key = api_key

    def run(self, prompt, code_snippet):
        if self.provider == "openai":
            return self._call_openai(prompt, code_snippet)
        elif self.provider == "ollama":
            return self._call_ollama(prompt, code_snippet)
        elif self.provider == "anthropic":
            return self._call_claude(prompt, code_snippet)

    def _call_openai(self, prompt, code_snippet):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model,  # Par exemple "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt + "\n" + code_snippet}
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']

    def _call_ollama(self, prompt, code_snippet):
        url = f"{ollama_host}/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,  # Assurez-vous que 'self.model' utilise bien 'mistral' comme modèle
            "prompt": prompt + "\n" + code_snippet,
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)

        # Débogage: affichez la réponse avant de l'enregistrer
        print("Ollama Response:", response.json())

        return response.json().get("generated_text", "")

    def _call_claude(self, prompt, code_snippet):
        url = "https://api.anthropic.com/v1/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-1",  # Utilisez le modèle souhaité
            "prompt": prompt + "\n" + code_snippet,
            "max_tokens": 150
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("completion", "")
