import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = open('input1.txt', encoding="utf8").read()

# Tokenization

wtokens = nltk.word_tokenize(sentence)

print("============== Word  Tokenization ==============")
print(wtokens)

stokens = nltk.sent_tokenize(sentence)
print("\n============== Sentence  Tokenization ==============\n")
print(stokens)