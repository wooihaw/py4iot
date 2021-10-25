import requests
from random import gauss

# Example to send data to the RESTful API via the post method
url1 = 'http://localhost:5000/send_data'
t, h = gauss(28, 2), gauss(84, 5)
try:
    r1 = requests.post(url1, json={'temperature': t, 'humidity': h})
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
else:
    if r1.status_code == 200:
        print(r1.json())
    else:
        print('Error!')

# Example to receive data using the RESTful API via the get method
url2 = 'http://localhost:5000/get_data'
n = 15
try:
    r2 = requests.get(url2 + f'?n={n}')
    # r2 = requests.get(url2, params={'n': n})
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
else:
    if r2.status_code == 200:
        print(r2.json())
    else:
        print('Error!')
