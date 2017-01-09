#!/usr/bin/python
import urllib.request, sys, re

def main():
    content_file="page.html"
    directory="/home/ludo/down_page/"
    try:
        url=sys.argv[1]
    except IndexError:
        print("""Zla syntax! Spravna: python3 down_page.py "http://www.blahblah.com" """)
        sys.exit()
    try:
        download(url,content_file, directory)
    except:
        print("Zadany parameter nie je platna adresa web stranky!")
        print("""Zla syntax! Spravna: python3 down_page.py "http://www.blahblah.com" """)

def download(url,content_file, directory):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    try:
        src = page.read().decode('utf8')
    except UnicodeDecodeError:
        src = page.read()
    f=open(content_file, "w")
    f.write(str(src))
    f.close()
    download_image(url,directory,src)

def download_image(url,directory,src):    
    images = re.findall(r'([-\w]+\.(?:jpg|gif|png))', url)
    print(images)
    images.sort()
    for image in images:
        url=src+image
        try:
            pic_file = open(directory+image, "wb")
            urllib.request.urlretrieve(url, pic_file)
            pic_file.close() 
        except:
            print ('Error writing file ' + image)

main()
