import nltk
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
word_tokens = nltk.word_tokenize(input)
print(nltk.pos_tag(word_tokens))