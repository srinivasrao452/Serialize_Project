
import json
import requests
url = 'http://127.0.0.1:3344/employees/'

emp={
    "ename":"Reshab",
    "esal" : 85000,
    "eaddr" : "Koti"
}

# response = requests.get(url)

# response = requests.post(url, data=json.dumps(emp))


id = input('Enter any id :')
# response = requests.get(url+id+'/')

# response = requests.delete(url+id)

response = requests.put(url+id+'/',data=json.dumps(emp))

if response.status_code==200:
    print('Status code is :', response.status_code)
    print(response.json())

elif response.status_code==201:
    print('Status code is :', response.status_code)
    print(response.json())

elif response.status_code==204:
    print('Status code is :', response.status_code)
    print('Record deleted successfully')

elif response.status_code==400:
    print('Status code is :', response.status_code)
    print('Record not created.')

elif response.status_code==404:
    print('Status code is :', response.status_code)
    print('Record not available')

elif response.status_code==500:
    print('Status code is :', response.status_code)
    print('Server side response')

else:
    print(response.status_code)
    print('something wrong')
