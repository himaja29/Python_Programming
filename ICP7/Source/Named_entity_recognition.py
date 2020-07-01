import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = open('input1.txt', encoding="utf8").read()

stokens = nltk.sent_tokenize(sentence)
n = 0
for s in stokens:
    print(ne_chunk(pos_tag(word_tokenize(s))))