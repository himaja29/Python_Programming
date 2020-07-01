#POS
import nltk
from nltk.tokenize import word_tokenize
sentence = open('input1.txt', encoding="utf8").read()
text = nltk.word_tokenize(sentence)
print(nltk.pos_tag(text))