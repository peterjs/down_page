#!/usr/bin/python
import urllib.request, sys, re, os

def main():
    try:
        local_web_page="page.html"
        web_page_url=sys.argv[1]
        directory_to_download=sys.argv[2]
        if os.path.isdir(directory_to_download) is not True:
            make_directory_for_download(directory_to_download)
        data_from_web_page = download_web_page_data(web_page_url)
        write_web_page_content_to_local_file(data_from_web_page, local_web_page)
        download_images_from_web_page(directory_to_download, data_from_web_page,web_page_url)
    except:
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
    path=os.path.normpath(output_file)
    return os.path.join(directory,output_file)

def download_images_from_web_page(directory, data_from_web_page,url):    
    images=find_images_on_page(data_from_web_page)
    print("Stahujem obrazky. Cakajte prosim.")
    for image in images:
        image=(url+image)
        picture_name=join_path(directory, image)
        print(picture_name)
        picture_name=picture_name.replace("/","_")
        picture_name=os.path.join(directory, picture_name)
        try:
            urllib.request.urlretrieve(image, picture_name)
            if os.path.exists(picture_name)==True:
                os.rename(picture_name, ""+picture_name)
        #       picture_name=picture_name+"duplicit"
        except (ValueError, urllib.error.URLError):
            pass
    print("Stahovanie dokoncene.")

main()
