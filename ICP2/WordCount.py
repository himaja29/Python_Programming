fileName = input("Enter file name : ")
f = open(fileName,'r')
wordcount={}
for str in f.read().split():
    temp = str.lower()
    if temp not in wordcount:
        wordcount[temp] = 1
    else:
        wordcount[temp] += 1
print("Output written in file")
print(wordcount, file=open("output.txt", "w"))