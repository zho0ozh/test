from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getnewlinks(url):
    html = urlopen("http://baike.baidu.com"+url)
    soup = BeautifulSoup(html,"html.parser")
    return soup.findAll("a",href=re.compile("^(/item/)((?!:).)*$"))

link = getnewlinks("/item/Justin")
while len(link) > 0:
    newlink = link[random.randint(0, len(link) - 1)].attrs["href"]
    if newlink == '/item/史记·2016?fr=navbar':
        newlink = link[random.randint(0, len(link) - 1)].attrs["href"]
    print('http://baike.baidu.com'+newlink)
    f = open('baike.txt', 'a')
    baocun = str(newlink+'\n')
    f.write(baocun)
    link = getnewlinks(newlink)
