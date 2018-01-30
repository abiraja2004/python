import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Hans_Zimmer"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
a=soup.find('h1')
print(a.text)
b = soup.findAll('div',{'class' : "mw-parser-output"})
for div in b:
    p = div.find('table')
    print(p.text)
c = soup.findAll('body', {'class': "mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Hans_Zimmer rootpage-Hans_Zimmer skin-vector action-view"})
for body in c:
    print(body.text)
