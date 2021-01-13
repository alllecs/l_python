import requests

open('xxx.txt') as f
f.readline().strip()
url = 'https://stepic.org/media/attachments/course67/3.6.2/603.txt'
f = requsts.get(url).text
print(f.splitlines())

#print(requests.get(open('xxx.txt').readline().strip()).text.count('\n'))
