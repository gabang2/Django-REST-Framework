import requests

url = "http://127.0.0.1:8000/api/auth/"
response = requests.post(url, data={'username': "admin", "password": "admin1234"})
myToken = response.json()["token"]
header = {"Authorization": "Token " + myToken}
response = requests.get("http://127.0.0.1:8000/api/student_list/", headers=header)
print(response.text)
