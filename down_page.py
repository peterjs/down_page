#!/usr/bin/python
import urllib.request, sys, re

def main():
    content_file="page.html"
    directory=sys.argv[2]
    try:
        url=sys.argv[1]
    except IndexError:
        print("""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory" """)
        sys.exit()
    try:
        download(url,content_file, directory)
    except:
        print("""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory" """)

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

def download_image(url,directory,page):    
    images=re.findall('img .*?src="(.*?)"',page)
    images.sort()
    urllib.request.urlcleanup()
    for image in images:
        url=page+image
        try:
            pic_name=directory+image[7:]  # OK
            with open(pic_name, "wb") as local_file:
                urllib.request.retrieve(url, local_file)
        except:
            print ('Error writing file ' + image)

main()
