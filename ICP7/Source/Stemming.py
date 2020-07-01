import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

sentence = open('input1.txt', encoding="utf8").read()

stokens = nltk.sent_tokenize(sentence)
pStemmer = PorterStemmer()
for s in stokens:
    print(pStemmer.stem(s))

lStemmer = LancasterStemmer()
print(lStemmer.stem(sentence))
for s in stokens:
    print(lStemmer.stem(s))

sStemmer = SnowballStemmer('english')
print(lStemmer.stem(sentence))
for s in stokens:
    print(sStemmer.stem(s))
