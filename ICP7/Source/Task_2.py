from bs4 import BeautifulSoup
import urllib.request


def search_spider():

    url = "https://en.wikipedia.org/wiki/Google"
    source_code = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code, "html.parser")

    body = soup.find('div', {'class': 'mw-parser-output'})
    file.write(str(body.text))



file = open('input1.txt', 'a+', encoding='utf-8')
search_spider()