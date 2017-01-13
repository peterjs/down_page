#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    content_file="page.html"
    directory=sys.argv[2]
    try:
        url=sys.argv[1]
    except IndexError as e:
        print(e,"""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory" """)
        sys.exit()
    download(url,content_file, directory)

def download(url,content_file, directory):  # OK
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    try:
        src = page.read().decode('utf8')
    except UnicodeDecodeError:
        src = page.read()
    with open(content_file,"w") as local_page:
        local_page.write(src)
    download_image(url,directory,src)  # fcia prebehne

def download_image(url,directory,page):    
    images=re.findall('img .*?src="(.*?)"',page)  # OK
    for image in images:
        url=(image)
        stripped_image_path=image[7:]
        pic_name=os.path.join(directory,os.path.basename(image) )
        print(pic_name)
        with open(pic_name, "wb") as local_file:
        #    data=urllib.request.urlretrieve(url, local_file)
        #    print(data)

main()
