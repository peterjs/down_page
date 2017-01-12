#!/usr/bin/python
import urllib.request, sys, re

def main():
    content_file="page.html"
    directory=sys.argv[2]
    try:
        url=sys.argv[1]
    except IndexError as e:
        print(e,"""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory" """)
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
    with open(content_file,"w") as local_page:
        local_page.write(src)
#    try:
    download_image(url,directory,src)  # fcia prebehne
#    except:
#        print("download_image() error.")

def download_image(url,directory,page):    
    print(images=re.findall('img .*?src="(.*?)"',page))
    print(images.sort())
    for image in images:
        url=page+image
        pic_name=directory+image[7:] 
        try:
            data=urllib.urlretrieve(url, local_file)
            with open(pic_name, "wb") as local_file:  # niekde v tomto je zrada
                local_file.write(data)
        except:
            print ('Error writing file ' + image)

main()
