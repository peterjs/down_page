#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        local_web_page="page.html"
        web_page_url=sys.argv[1]
        directory_to_download=sys.argv[2]
        data_from_web_page = download_web_page_data(web_page_url, local_web_page, directory_to_download)
        write_web_page_content_to_local_file(data_from_web_page, local_web_page)
        download_images_from_web_page(directory_to_download, data_from_web_page)
    except:
           print("""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory_to_download" """)

def download_web_page_data(web_page_url, local_web_page, directory_to_download):
    request_to_page = urllib.request.Request(web_page_url)
    web_page = urllib.request.urlopen(request_to_page)
    try:
        return web_page.read().decode('utf8')
    except UnicodeDecodeError:
        return web_page.read()

def write_web_page_content_to_local_file(data_from_web_page, local_web_page):
    with open(local_web_page,"w") as local_page:
        local_page.write(data_from_web_page)
    print("Stranka stiahnuta.")

def find_images_on_page(data_from_web_page):
    img=re.findall('img .*?src="(.*?)"',data_from_web_page)
    return img

def download_images_from_web_page(directory_to_download, data_from_web_page):    
    images_on_web_page=find_images_on_page(data_from_web_page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images_on_web_page:
        local_picture=os.path.join(directory_to_download,os.path.basename(image))
        try:
            urllib.request.urlretrieve(image, local_picture)
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
