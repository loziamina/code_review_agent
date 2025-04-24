import argparse
from agent.analyzer import CodeAnalyzer
from agent.llm_interface import LLMClient

def main():
    # Configuration de l'argument parser
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--file", required=True, help="Path to the Python file to review")
    parser.add_argument("--mode", default="strict", choices=["strict", "mentor", "test_focus"], help="Review mode")
    parser.add_argument("--provider", default="openai", choices=["openai", "ollama", "anthropic"], help="LLM provider")
    args = parser.parse_args()

    # Lire le code à partir du fichier
    with open(args.file, "r") as file:
        code_snippet = file.read()

    # Initialiser le client LLM
    llm_client = LLMClient(provider=args.provider, model="text-davinci-003", api_key="your-api-key")

    # Initialiser l'analyseur de code
    analyzer = CodeAnalyzer(mode=args.mode)

    # Analyser le code
    review = analyzer.analyze_code(code_snippet, llm_client)

    # Sauvegarder la révision dans un fichier
    with open("reviews/review_output.md", "w") as review_file:
        review_file.write(review)

    print("Review saved to reviews/review_output.md")

if __name__ == "__main__":
    main()
