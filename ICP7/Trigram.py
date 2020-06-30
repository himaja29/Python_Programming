import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
sent_tokens = nltk.sent_tokenize(input)
for i in sent_tokens:
    word_tokens = nltk.word_tokenize(i)
    for j in range(len(word_tokens)-2):
        print(word_tokens[j], word_tokens[j + 1], word_tokens[j + 2])
