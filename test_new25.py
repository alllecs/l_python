import requests

res = requests.get("http://docs.python.org/3.5/")
print(res.status_code)
print(res.headers['Content-Type'])

#print(res.content)
#print(res.text)

res = requests.get("http://docs.python.org/3.5/_static/py.png")
print(res.content)

with open("python.png", "wb") as f:
    f.write(res.content) #get image
