import spacy  # Import spaCy for natural language processing

# Load English language model (run `python -m spacy download en_core_web_sm` first)
nlp = spacy.load("en_core_web_sm")

# Function to analyze the command and return tokenized words
def analyze_command(text):
    doc = nlp(text)  # Process the text input
    return [token.text for token in doc]  # Return each word (token) as a list
