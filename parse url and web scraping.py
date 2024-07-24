import requests
from bs4 import BeautifulSoup

data=requests.get('https://www.wscubetech.com/')
soup=BeautifulSoup(data.content,'html.parser')
for a in soup.find_all('a'):
    print(soup.a)
 
