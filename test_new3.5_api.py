import requests
import json

client_id = '7542626e111794676ec7'
client_secret = 'fcdb525d961a33fdcdf1731ac9c104cc'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
        data={
            "client_id": client_id,
            "client_secret": client_secret
            })
# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
dict_artist = {}
with open("dataset_244.txt") as f:
    line = f.read().split()
for n in line:
    n = n.strip()
    headers = {"X-Xapp-Token" : token}
    r = requests.get("https://api.artsy.net/api/artists/{n}".format(n = n), headers=headers)
    r.encoding = 'utf-8'
    j = json.loads(r.text)
    #print(j['sortable_name'], j['birthday'])
    dict_artist[j["sortable_name"]] = j['birthday']

#print(sorted(dict_artist.items(), key=lambda x: (x[1], x[0])))
d_list = list(dict_artist.items())
d_list.sort(key=lambda x: (x[1], x[0]))
for i in d_list:
    print(i[0])
