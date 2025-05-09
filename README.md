# Spelling Error Correction with LLM

This project uses a Language Model (via Ollama) to correct spelling errors in sentences and evaluates the model's accuracy.

## Setup

### Local Setup

1. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install Ollama following instructions at https://ollama.com/

3. Pull the desired model:
   ```
   ollama pull llama3
   ```

### Google Colab Setup

1. Upload all files to Colab

2. Install required libraries and Ollama:
   ```python
   !pip install requests numpy matplotlib Levenshtein
   !curl -fsSL https://ollama.com/install.sh | sh
   !ollama serve &
   !ollama pull llama3
   ```

## Usage

Run the main script:

