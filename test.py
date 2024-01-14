import requests

url = "http://localhost:3000/transaction"
data = {"amount": 100}  # Change this value based on your transaction amount

response = requests.post(url, json=data)

print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
