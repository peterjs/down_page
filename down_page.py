#!/usr/bin/python
import urllib.request, sys, re

def main():
    content_file="page.html"
    directory=sys.argv[2]
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
    images=re.findall('img .*?src="(.*?)"',src)
    images.sort()
    for image in images:
        url=src+image
        try:
            pic_name=directory+image[7:]  # OK
            pic_file = open(pic_name, "wb")
            pic=urllib.request.urlopen(url).read()
            pic_file.write(pic)
            #urllib.urlretrieve(url, pic_file)
            #pic_file.write(urllib.requst.urlopen(image).read())
            pic_file.close() 
        except:
            print ('Error writing file ' + image)

main()
