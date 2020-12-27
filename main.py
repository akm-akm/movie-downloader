from bs4 import BeautifulSoup
import urllib.request
import re
import pyautogui
import os
import time
f = open('list.txt', 'r')
d = open("notfound.txt", "a")
fd = open("found.txt", "a")


for x in f:
    c= 'fe'   
    fg=x    
    x=x.strip()
    x=x.replace(" ","%20")
    x = "https://piratebay.party/search/" + x + "/1/99/0"
    html_page = urllib.request.urlopen(x)
    soup = BeautifulSoup(html_page,'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^magnet:")}):
        c=link.get('href')
        break 

    if c!='fe':

       os.startfile(c)
       print("Added",fg)
       fd.write(fg)


    else:

       print("Not added",fg)
       d.write(fg)

f.close()
d.close()
fd.close()

