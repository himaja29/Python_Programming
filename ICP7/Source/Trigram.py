#trigram
import nltk
from nltk.util import ngrams
sentence = open('input1.txt', encoding="utf8").read()
tokens = nltk.word_tokenize(sentence)
trigrams = list(ngrams(tokens, 3))
print(trigrams)
