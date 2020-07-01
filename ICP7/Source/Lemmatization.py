# Lemmatization
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
sentence = open('input1.txt', encoding="utf8").read()
stokens = nltk.sent_tokenize(sentence)
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

for s in stokens:
    print(lemmatizer.lemmatize(s))