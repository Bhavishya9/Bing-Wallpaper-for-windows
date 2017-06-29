import re
import os
import time
import json
import requests
import urllib
import ctypes
import socket

def wallpaper():
    # this url because bing uses this url to load the image you can see this if use Fiddler application
    URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    image_data = json.loads(requests.get(URL).text)
    image_url = 'http://www.bing.com' + image_data['images'][0]['url']
    image_download_url = 'http://www.bing.com/hpwp/' + image_data['images'][0]['hsh']
    image_name = image_url[re.search("rb/", image_url).end():re.search('_EN', image_url).start()] + '.jpg'
    filepath = "C:\Users\Admin\Pictures\Bing_Wallpapers" + "\\" + image_name
    urllib.urlretrieve(image_download_url, filename=filepath)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath, 0)
    return 0

def internet(host="8.8.8.8", port=53, timeout=3):

   #Host: 8.8.8.8 (google-public-dns-a.google.com)
   #OpenPort: 53/tcp
   #Service: domain (DNS/TCP)
   try:
     socket.setdefaulttimeout(timeout)
     socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
     return True
   except Exception as ex:
     print ex.message
     return False
try:
  call=wallpaper()
except:
    while(1):
        if(internet()):
            break
    call=wallpaper()


