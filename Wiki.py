# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime,random,re,os,requests,urllib

pages=set()
imgs=set()
html=urlopen("http://www.meizitu.com")
soup =BeautifulSoup(html,"html.parser")

cishu=0
targetPath = "H:\\Codepage\\img"

def saveFile(path):
    #检测当前路径的有效性
    global cishu
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    #设置每个图片的路径
    cishu = cishu+1
    pos = path.rindex('/')
    t = os.path.join(targetPath, str(cishu)+".jpg")
    print(t)
    return t

def downImg(data):
    for link,t in set(re.findall(r'([http|https]:[^\s]*?(jpg|png|gif))', str(data))):

        if link.startswith('s'):
            link='http'+link
        else:
            link='htt'+link
        print(link)
        try:
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(link,str(saveFile(link)))
        except:
            print('失败')

def getlinks(url):
    global pages
    html=urlopen("http://www.meizitu.com")
    soup = BeautifulSoup(html,"html.parser")
    for link in soup.findAll("a"):
        if 'href' in link.attrs:
            if link.attrs['href'][0:15]=='http://www.meiz':
                if link.attrs['href'] not in pages:
                    newPage =link.attrs['href']
                    pages.add(newPage)
                    getlinks(newPage)
                    html=urlopen(newPage)
                    soup=BeautifulSoup(html,"html.parser")
                    for img in soup.findAll("img"):
                        if 'src' in img.attrs:
                            if img.attrs['src'] not in imgs:
                                imgs.add(img.attrs['src'])
                                print(img.attrs['src'])
                                downImg(img.attrs['src'])



getlinks("")
