import nltk
#punkt sentence tokenizer divides the text into list of sentences
nltk.download('punkt')
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
sent_tokens = nltk.sent_tokenize(input)
word_tokens = nltk.word_tokenize(input)
for s in sent_tokens:
    print(s)
for t in word_tokens:
    print(t)