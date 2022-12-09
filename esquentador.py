import requests
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
  '22988523276',
  '32991273468',
  '32991284917',
  '61993806149',
  '32991263020',
  '32984015683'
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