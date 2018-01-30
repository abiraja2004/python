import requests
from bs4 import BeautifulSoup
import os

page = "https://weather.com/weather/today/l/64123:4:US"
source_code = requests.get(page)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'html.parser')
"""print(soup.prettify())"""
print(list(soup.children))
"""print([type(item) for item in list(soup.children)])"""
html = list(soup.children)
list(html.children)
