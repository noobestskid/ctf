import requests
import re

FLAG = ""
URL = "http://89.38.210.129:8015/"

def solve():
    global FLAG
    global URL

    session = requests.Session()
    while True:
        response = session.request('HEAD', URL)
        if response.status_code == 200:
            headers = response.headers
            letter1 = headers['X-Data']
            # letter2 is found in the Set-Cookie header
            letter2 = re.search(r'Data-X=(.+)', headers['Set-Cookie']).group(1)
            FLAG += letter1 + letter2
            # %7D means }
            # it is our stop condition
            if letter1 == '%7D' or letter2 == '%7D':
                break
        else:
            pass
    print("FLAG: ", FLAG.replace('%7D', '}'))

if __name__ == "__main__":
    solve()