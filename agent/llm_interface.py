import openai
import requests
import anthropic

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
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt + "\n" + code_snippet,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def _call_ollama(self, prompt, code_snippet):
        url = "http://127.0.0.1:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,
            "prompt": prompt + "\n" + code_snippet,
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("generated_text", "")

    def _call_claude(self, prompt, code_snippet):
        url = "https://api.anthropic.com/v1/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-1",
            "prompt": prompt + "\n" + code_snippet,
            "max_tokens": 150
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("completion", "")
