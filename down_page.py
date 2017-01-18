#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        local_web_page="page.html"
        directory_to_download=sys.argv[2]
        web_page_url=sys.argv[1]
        web_page_name=local_web_page_name(directory_to_download, local_web_page)
        if os.path.isdir(directory_to_download) is not True:
            make_directory_for_download(directory_to_download)
        data_from_web_page = download_web_page_data(web_page_url)
        write_web_page_content_to_local_file(data_from_web_page, web_page_name)
        download_images_from_web_page(directory_to_download, data_from_web_page)
    except:
        help_syntax()

def local_web_page_name(directory, name):
    return os.path.join(directory,directory+"_"+name)

def help_syntax():
    print("""Syntax: python down_page.py http://www.name_of_page.com local_directory_to_download """)
    print("""Syntax: python3 down_page.py http://www.name_of_page.com local_directory_to_download """)
    print("""Syntax: python.exe down_page.py http://www.name_of_page.com local_directory_to_download """)

def make_directory_for_download(directory):
    os.mkdir(directory)
         
def open_web_page(url):
    request_to_page = urllib.request.Request(url)
    return urllib.request.urlopen(request_to_page)

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

def join_path(directory, output_file):
    return os.path.join(directory,os.path.basename(output_file))

def rename_picture(picture):
        return os.rename(picture, "x"+picture)

def retrieve_image_from_web(image, name):
    return urllib.request.urlretrieve(image, name)

def find_duplicit_images():
    return

def download_images_from_web_page(directory, data_from_web_page):    
    images=find_images_on_page(data_from_web_page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images:
        picture_name=join_path(directory, image)
        try:
            if os.path.isfile(picture_name) is True:
                picture_name=rename_picture(picture_name)
            retrieve_image_from_web(image, picture_name)
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
