#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        content_file="page.html"
        directory=sys.argv[2]
        try:
            url=sys.argv[1]
        except IndexError as e:
            print(e,"""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory" """)
            sys.exit()
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
    with open(content_file,"w") as local_page:
        local_page.write(src)
    print("Stranka stiahnuta.")
    download_image(url,directory,src)

def download_image(url,directory,page):    
    images=re.findall('img .*?src="(.*?)"',page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images:
        url=(image)
        stripped_image_path=image[7:]
        pic_name=os.path.join(directory,os.path.basename(image) )
        try:
            data=urllib.request.urlretrieve(url, pic_name)
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
