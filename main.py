import time
import matplotlib.pyplot as plt
from ollama_client import OllamaClient
from metrics import exact_match_accuracy, character_level_accuracy, word_level_accuracy
from data import get_sample_indonesian_dataset

# Install dependencies for Google Colab (uncomment when running in Colab)
# !pip install requests numpy matplotlib Levenshtein

# Setup Ollama in Colab (uncomment when running in Colab)
# !curl -fsSL https://ollama.com/install.sh | sh
# !ollama serve &  # Start Ollama service

def main():
    # Initialize the Ollama client
    client = OllamaClient()
    
    # Get the dataset
    dataset = get_sample_indonesian_dataset()
    error_sentences = dataset.error_sentences
    correct_sentences = dataset.correct_sentences
    
    print(f"Dataset loaded with {len(dataset)} samples.")
    
    # Pull the model if needed (uncomment when running in Colab)
    # !ollama pull llama3
    
    # Correct spelling errors using the LLM
    corrected_sentences = []
    processing_times = []
    
    print("\nProcessing sentences...")
    for i, error_sentence in enumerate(error_sentences):
        start_time = time.time()
        
        # Get correction from LLM
        corrected = client.correct_spelling(error_sentence)
        
        end_time = time.time()
        processing_time = end_time - start_time
        processing_times.append(processing_time)
        
        corrected_sentences.append(corrected)
        
        print(f"Sample {i+1}:")
        print(f"  Error:     '{error_sentence}'")
        print(f"  Correct:   '{correct_sentences[i]}'")
        print(f"  Corrected: '{corrected}'")
        print(f"  Time: {processing_time:.2f}s")
        print("")
    
    # Calculate accuracy metrics
    exact_acc = exact_match_accuracy(corrected_sentences, correct_sentences)
    char_acc = character_level_accuracy(corrected_sentences, correct_sentences)
    word_acc = word_level_accuracy(corrected_sentences, correct_sentences)
    
    print("\n--- Results ---")
    print(f"Exact Match Accuracy: {exact_acc:.4f}")
    print(f"Character-level Accuracy: {char_acc:.4f}")
    print(f"Word-level Accuracy: {word_acc:.4f}")
    print(f"Average Processing Time: {sum(processing_times) / len(processing_times):.2f}s")
    
    # Visualize accuracy metrics
    metrics = ['Exact Match', 'Character-level', 'Word-level']
    values = [exact_acc, char_acc, word_acc]
    
    plt.figure(figsize=(10, 6))
    plt.bar(metrics, values, color=['blue', 'green', 'orange'])
    plt.ylim(0, 1.0)
    plt.title('LLM Spelling Correction Accuracy')
    plt.ylabel('Accuracy')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(values):
        plt.text(i, v + 0.02, f'{v:.4f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('accuracy_metrics.png')
    plt.show()

if __name__ == "__main__":
    main()
