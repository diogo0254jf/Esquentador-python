import requests
import time
from numpy import random

portas = [
  '8000',
  '8002',
  '8003',
  '8004',
  '8005',
  '8006'
]

numeros = [
  '32984015683',
  '32991263020',
  '22988523276',
  '32991282409',
  '61993806149',

  '32991273468'
]
for v in portas:
  for k in numeros:
    time.sleep(1)
    url = f"http://20.81.42.82:{v}/send-message"
    
    payload = {
          'number': f'{k}',
          'message': 'oi'
      }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url,headers=headers, data=payload)
    print(response.text)