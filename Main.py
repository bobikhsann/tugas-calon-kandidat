import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.pikiran-rakyat.com/'
headers = {
   'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

data = []
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('div', 'most__item')
for it in items:
    judul = ''.join (it.find('div', 'most__right').text.strip().split('\n'))
    data.append([judul])
    

kepalatabel = ['JUDUL BERITA TERPOPULER']   
writer = csv.writer(open('pikiranrakyat.csv', 'w', newline=""))
writer.writerow(kepalatabel)
for d in data : writer.writerow(d)    

