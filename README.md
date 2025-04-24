````markdown
# AI Code Review Agent

This project aims to create a Python-based AI agent that reviews code. The agent analyzes code snippets or files, detects potential issues, suggests improvements, and generates a review summary.

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [API Keys](#api-keys)
6. [Troubleshooting](#troubleshooting)

## Requirements

- Python 3.7 or higher
- `pip` for installing dependencies
- OpenAI API Key
- Anthropic API Key (optional)
- Ollama (optional, for local models)

## Installation

Follow these steps to install and set up the project.

### 1. Clone the repository

Clone the project to your local machine:

```bash
git clone https://github.com/loziamina/code_review_agent.git
cd code_review_agent
```
````

### 2. Set up a virtual environment (optional but recommended)

It's recommended to create a virtual environment to avoid dependency conflicts.

```bash
python -m venv venv
venv\Scripts\activate`
```

### 3. Install dependencies

Install the required dependencies from **`requirements.txt`**:

```bash
pip install -r requirements.txt
```

### 4. Install OpenAI Python client

Make sure you have the OpenAI Python client installed:

```bash
pip install openai
```

If you are using Ollama, ensure that you have it running locally (refer to the Ollama documentation for setup).

## Configuration

### 1. Set up the API keys

Create a **`config.yaml`** file in the root of the project with your API keys and configuration settings:

```yaml
openai_api_key: "your-openai-api-key"
anthropic_api_key: "your-anthropic-api-key"

# Ollama configuration
ollama_host: "http://127.0.0.1:11434" # Local Ollama server
ollama_model: "llama3.2" # Set to the model you are using in Ollama

OLLAMA_CONTEXT_LENGTH: 2048
OLLAMA_MAX_LOADED_MODELS: 0
OLLAMA_MAX_QUEUE: 512
OLLAMA_KEEP_ALIVE: "5m0s"
OLLAMA_NOHISTORY: false
```

### 2. Make sure to add **`config.yaml`** to `.gitignore` to keep your API keys secure:

```bash
echo "config.yaml" >> .gitignore
```

## Usage

To run the code review agent, use the following command:

### Basic command structure:

```bash
python cli.py --file <path-to-python-file> --mode <mode> --provider <openai|ollama|anthropic>

or

py cli.py --file <path-to-python-file> --mode <mode> --provider <openai|ollama|anthropic>

```

### Example commands:

- **Run with OpenAI:**

```bash
python cli.py --file examples/buggy_script.py --mode strict --provider openai

or

py cli.py --file examples/buggy_script.py --mode strict --provider openai

```

- **Run with Ollama:**

```bash
python cli.py --file examples/buggy_script.py --mode mentor --provider ollama

or

py cli.py --file examples/buggy_script.py --mode mentor --provider ollama

```

- **Run with Anthropic:**

```bash
python cli.py --file examples/buggy_script.py --mode test_focus --provider anthropic

or

py cli.py --file examples/buggy_script.py --mode test_focus --provider anthropic

```

### Modes:

- `strict`: Strict review with detailed feedback.
- `mentor`: Act as a mentor to guide and provide learning suggestions.
- `test_focus`: Focus on identifying missing or weak test cases.

## API Keys

You need valid API keys to interact with the services:

- **OpenAI API Key**: Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys) to create a new key.
- **Anthropic API Key** (optional): Go to [Anthropic API](https://www.anthropic.com) to get a key if using Claude for reviews.
- **Ollama**: If you use Ollama locally, you need to have it running on your machine.

## Troubleshooting

### 1. **API Key Authentication Error**

If you encounter an `AuthenticationError` when using OpenAI, Anthropic, or Ollama, double-check that the API key is correct and properly set in **`config.yaml`**.

### 2. **Ollama Not Running**

If you're using Ollama and it’s not working, ensure you have started the Ollama server:

```bash
ollama serve
```

Make sure the server is running on the correct port and the host matches the one in your **`config.yaml`**.

### 3. **Missing `pip` or Other Tools**

If you encounter issues related to `pip` or other tools, make sure they are correctly installed and that your virtual environment is activated.

```bash
python -m ensurepip --upgrade
```

### 4. **Error with Required Libraries**

If the libraries in **`requirements.txt`** are not installed correctly, try upgrading `pip`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
