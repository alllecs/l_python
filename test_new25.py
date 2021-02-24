import requests

res = requests.get("http://docs.python.org/3.5/")
print(res.status_code)
print(res.headers['Content-Type'])
