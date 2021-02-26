import requests

api_url = 'http://numbersapi.com/{n}/math'


params = {
        'json': 'true',
        'callback': 'showNumber'
        }
with open("fileinput.txt") as f:
    num = f.read().split()
for n in num:
    url = api_url.format(n=n)
    res = requests.get(url, params=params)
    data = res.json()
    if data["found"]:
        print("Interesting")
    else:
        print("Boring")

"""
#second solution
with open('dataset_24476_3.txt') as file:
    for num in file:
        response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()
        print('Interesting') if response['found'] else print('Boring')
"""


#print(res.status_code)
#print(res.headers["Content-Type"])
