import requests
import re
from bs4 import BeautifulSoup as BS

def get_request(url):
    url2 = str(input())
    res = requests.get(url)
    if res.status_code == 200:
        soup = BS(res.text, "html.parser")
        links = soup.find_all('a') #найти все ссылки
        for link in links:
            res2 = requests.get(str(link)[9:-7])
            if res2.status_code == 200:
                soup = BS(res2.text, "html.parser")
                links = soup.find_all('a')
                for link in links:
                    if str(link)[9:-7] == url2:
                        return "Yes"
    return "No"
            
url1 = str(input())
print(get_request(url1))

#Second version
"""
start_url = input()
end_url = input()
found = False

link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

resp = requests.get(start_url).text
for url in link_pattern.findall(resp):
    cur_resp = requests.get(url).text
    if end_url in link_pattern.findall(cur_resp):
        found = True
        break

print("Yes" if found else "No")
"""
