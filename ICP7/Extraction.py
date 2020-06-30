import requests
link = 'https://en.wikipedia.org/wiki/Google'
response = requests.get(link)
from bs4 import BeautifulSoup
content = BeautifulSoup(response.content, "html.parser")
text = content.get_text()
print(text)
f = open('input.txt', 'w',encoding='utf-8')
f.write(text)
