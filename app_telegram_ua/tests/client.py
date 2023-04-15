import requests

data = {
    'order_id': '60bc8b3d539e95756f068d33',
    'order_status': 'approved',
}

HOST = 'http://localhost:8080'

resp = requests.post(f'{HOST}/payment', json=data)
print(resp.text)
