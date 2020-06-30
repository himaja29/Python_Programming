from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
word_tokens = nltk.word_tokenize(input)
lemmatizer = WordNetLemmatizer()
for x in word_tokens:
    print(lemmatizer.lemmatize(x))