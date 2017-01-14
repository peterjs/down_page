#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        local_web_page="page.html"
        web_page_url=sys.argv[1]
        directory_to_download=sys.argv[2]
        data_from_web_page = download_web_page_data(web_page_url)
        write_web_page_content_to_local_file(data_from_web_page, local_web_page)
        download_images_from_web_page(directory_to_download, data_from_web_page)
    except:
           print("""Syntax: python3 down_page.py "http://www.name_of_page.com" "local_directory_to_download" """)

def open_web_page(url):
    request_to_page = urllib.request.Request(url)
    page = urllib.request.urlopen(request_to_page)
    return page

def download_web_page_data(url):
    content= open_web_page(url) 
    try:
        return content.read().decode('utf8')
    except UnicodeDecodeError:
        return content.read()

def write_web_page_content_to_local_file(data, destination):
    print("Stahujem stranku.")
    with open( destination,"w") as local_file:
        local_file.write(data)
    print("Stranka stiahnuta.")

def find_images_on_page(data):
    img=re.findall('img .*?src="(.*?)"',data)
    return img

def download_images_from_web_page(directory, data_from_web_page):    
    images=find_images_on_page(data_from_web_page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images:
        picture_name=os.path.join(directory,os.path.basename(image))
        try:
            urllib.request.urlretrieve(image, picture_name)
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
