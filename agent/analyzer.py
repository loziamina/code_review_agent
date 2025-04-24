import yaml
from agent.llm_interface import LLMClient

class CodeAnalyzer:
    def __init__(self, mode="strict"):
        # Charger les modèles de prompts depuis le fichier YAML
        with open("prompts/templates.yaml", "r") as f:
            self.prompts = yaml.safe_load(f)
        self.mode = mode

    def generate_prompt(self, code_snippet):
        # Générez un prompt basé sur le mode de révision choisi
        prompt_template = self.prompts.get(self.mode, {})
        description = prompt_template.get("description", "")
        return f"{description}\nCode:\n{code_snippet}"

    def analyze_code(self, code_snippet, llm_client):
        # Crée le prompt à partir du code
        prompt = self.generate_prompt(code_snippet)
        # Envoie le prompt à l'API LLM pour analyse
        return llm_client.run(prompt, code_snippet)
