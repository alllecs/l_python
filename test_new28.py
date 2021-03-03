import wget
import re
import itertools
import requests
from bs4 import BeautifulSoup as BS

#filename = wget.download("http://pastebin.com/raw/7543p0ns")
#filename = wget.download("http://pastebin.com/raw/hfMThaGb", bar=None)
#filename = wget.download(str(input()), bar=None)
#filename = "7543p0ns"

url = str(input())

new = []
#link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
link_pattern = re.compile(r'<a[^>]*?href=[\"|\']([\w|\.|\-]+://)?([a-zA-Z][\w|\.|\-]+)')
resp = requests.get(url).text
for link in link_pattern.findall(resp):
    if not link[1] in new:
        new.append(link[1])

new = sorted(new)
for i in new:
    print(i)

"""
x = []
with open(filename) as f:
    for i in f:
        i = i.strip()
        x.append(re.findall(r'href=[\"|\']([\w|\.|\-]+://)?([a-zA-Z][\w|\.|\-]+)', i))

new = []
for i in x:
    if i:
        if not i[0][1] in new:
            new.append(i[0][1])
new = sorted(new)
for i in new:
    print(i)
"""
