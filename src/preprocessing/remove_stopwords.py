import nltk
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(text):
    words = word_tokenize(text)
    sw = set(stopwords.words('english'))
    filtered = [w for w in words if w not in sw]
    return " ".join(filtered)