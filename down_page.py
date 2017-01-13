#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        local_web_page="page.html"
        web_page_url=sys.argv[1]
        directory_to_download=sys.argv[2]
        download(web_page_url, local_web_page, directory_to_download)
    except:
           print("""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory_to_download" """)

def download(web_page_url, local_web_page, directory_to_download):
    request_to_page = urllib.request.Request(web_page_url)
    web_page = urllib.request.urlopen(request_to_page)
    try:
        data_from_web_page= web_page.read().decode('utf8')
    except UnicodeDecodeError:
        data_from_web_page = web_page.read()
    with open(local_web_page,"w") as local_page:
        local_page.write(data_from_web_page)
    print("Stranka stiahnuta.")
    download_images_from_web_page(directory_to_download, data_from_web_page)

def download_images_from_web_page(directory_to_download, data_from_web_page):    
    images_on_web_page=re.findall('img .*?src="(.*?)"',data_from_web_page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images_on_web_page:
        web_picture_url=image
        local_picture=os.path.join(directory_to_download,os.path.basename(image))
        try:
            urllib.request.urlretrieve(web_picture_url, local_picture)
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
