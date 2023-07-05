# Web scrapping using BeautifulSoup

import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Free cat pics 
source = requests.get('https://www.freeimages.com/search/cat', headers=headers).text
soup = BeautifulSoup(source, 'lxml')

Images =[]
img_links = soup.select('img[src^="https://www.freeimages.com/"]')
for i in range(len(img_links)):
    Images.append(img_links[i]['src'])

print(Images)

for i in range(len(Images)):
    name="add file path to store downloaded gifs here"+str(i)+".jpg" #change to png/ gif/ etc depending on requirement 
    urllib.request.urlretrieve(Images[i], name)


