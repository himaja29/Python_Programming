import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
word_tokens = nltk.word_tokenize(input)
pStemmer = PorterStemmer()
print(pStemmer.stem('greater'))

lStemmer = LancasterStemmer()
print(lStemmer.stem('greater'))

sStemmer = SnowballStemmer('english')
print(sStemmer.stem('greater'))
