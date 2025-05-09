class SpellingDataset:
    def __init__(self, error_sentences=None, correct_sentences=None):
        """
        Initialize the dataset with error sentences and their corrections.
        
        Args:
            error_sentences (list): List of sentences with spelling errors
            correct_sentences (list): List of corrected sentences
        """
        self.error_sentences = error_sentences or []
        self.correct_sentences = correct_sentences or []
        
    def add_sample(self, error_sentence, correct_sentence):
        """Add a sample to the dataset."""
        self.error_sentences.append(error_sentence)
        self.correct_sentences.append(correct_sentence)
        
    def get_sample(self, index):
        """Get a sample pair by index."""
        if 0 <= index < len(self.error_sentences):
            return self.error_sentences[index], self.correct_sentences[index]
        return None, None
    
    def get_all_samples(self):
        """Get all samples as pairs."""
        return list(zip(self.error_sentences, self.correct_sentences))
    
    def __len__(self):
        """Get the size of the dataset."""
        return len(self.error_sentences)

# Sample Indonesian spelling error dataset
def get_sample_indonesian_dataset():
    """
    Create a sample Indonesian dataset with spelling errors and corrections.
    
    Returns:
        SpellingDataset: A dataset with error-correction pairs
    """
    dataset = SpellingDataset()
    
    # Add sample pairs (error_sentence, correct_sentence)
    dataset.add_sample("Saya Belajaaar Apa", "Saya Belajar Apa")
    dataset.add_sample("Dia mkan nasi goreng kemren", "Dia makan nasi goreng kemarin")
    dataset.add_sample("Aku prgi ke sekola tiap pagi", "Aku pergi ke sekolah tiap pagi")
    dataset.add_sample("Ibuku maseh memaska di dpur", "Ibuku masih memasak di dapur")
    dataset.add_sample("Kmaren sya bermian bola dngan teman", "Kemarin saya bermain bola dengan teman")
    dataset.add_sample("Bapak sdeng membersiihkan moblnya", "Bapak sedang membersihkan mobilnya")
    dataset.add_sample("Adik sya menangiss karna jatuh", "Adik saya menangis karena jatuh")
    dataset.add_sample("Kuching itu berlrai cepet sekali", "Kucing itu berlari cepat sekali")
    dataset.add_sample("Kakak membelii bukuu itu kemarn", "Kakak membeli buku itu kemarin")
    dataset.add_sample("Kami perrgi ke pantay waktu liburran", "Kami pergi ke pantai waktu liburan")
    
    return dataset
