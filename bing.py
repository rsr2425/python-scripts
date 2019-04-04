#! /usr/bin/python3
 
import requests
from bs4 import BeautifulSoup
import os
import datetime
from appscript import app, mactypes
 
dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
try:
    os.makedirs('Bing')
except OSError as exc:
    pass
url = 'http://bingwallpaper.com/' 
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
image = soup.select('.cursor_zoom img')
image_url = image[0].get('src')
res = requests.get(image_url)
with open(os.path.join('Bing',cd+'.jpg'),'wb') as file:
    file.write(res.content)
command_to_run = """osascript -e 'tell application "Finder" to set desktop picture to "/Users/Ryan/Dropbox/Code/Scripts/Bing/%s" as POSIX file'""" %(cd + '.jpg')
os.system(command_to_run)
