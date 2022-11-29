import requests
import time
from numpy import random

portas = [
  '7000',
  '7002',
  '7003',
  '7004',
  '7005',
  '7006'
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
    
    url = f"http://localhost:{v}/send-message"
    
    payload = {
          'number': f'{k}',
          'message': 'oi'
      }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url,headers=headers, data=payload)
    print(response.text)