#!/usr/bin/python
import urllib.request, sys, re, os, base64

def main():
    try:
        local_web_page="page.html"
        web_page_url=sys.argv[1]
        directory_to_download=sys.argv[2]
        if os.path.isdir(directory_to_download) is not True:
            make_directory_for_download(directory_to_download)
        data_from_web_page = download_web_page_data(web_page_url)
        write_web_page_content_to_local_file(data_from_web_page, local_web_page,directory_to_download)
        download_images_from_web_page(directory_to_download, data_from_web_page,web_page_url)
    except:
           help_syntax()

def help_syntax():
    print("""Syntax (python 3.x) : python3 down_page.py http://www.name_of_page.com local_directory_to_download """)
    print("""Syntax (Windows)    : python.exe down_page.py http://www.name_of_page.com local_directory_to_download """)
    print("""Skript nefunguje s python 2.x""")

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

def write_web_page_content_to_local_file(data, destination, directory):
    print("Stahujem stranku.")
    downloaded_file=os.path.join(directory,destination)
    with open(downloaded_file,"w") as local_file:
        local_file.write(data)
    print("Stranka stiahnuta.")

def compare_web_page_content(url,directory,destination):
    actual_content=download_web_page_data(url)
    local_content=os.path.join(directory,destination)
    if local_content is not True:
        print("Nie je s cim porovnavat, web stranka nie je stiahnuta.")
    else:
        print("Porovnavam obsah.")
    return

def find_images_on_page(data):
    img=re.findall('img .*?src="(.*?)"',data)
    return img

def join_path(directory, output_file):
    path=os.path.normpath(output_file)
    return os.path.join(directory,output_file)

def create_file_name(directory, picture):
    name=join_path(directory, picture)
    name=name.replace("/","")
    name=os.path.join(directory, name)
    return name

def check_picture_url(url, picture):
    if "http" in picture:
        picture=picture
    else:
        picture=(url+picture)
    return picture

def base64_picture_download(picture_url, local_picture):
    picture=urllib.request.urlopen(picture_url)
    picture_read=picture_url.read()
    picture_64_encode = base64.encodestring(picture_read)
    picture_64_decode = base64.decodestring(picture_64_encode)
    picture_result = open(local_picture, 'wb')
    picture_result.write(picture_64_decode)

def download_images_from_web_page(directory, data_from_web_page,url):    
    try:
        images=find_images_on_page(data_from_web_page)
        print("Stahujem obrazky. Cakajte prosim.")
        for image in images:
            image = check_picture_url(url, image)
            picture_name=create_file_name(directory, image)
            try:
                if "base64" in image:
                    base64_picture_download(image, picture_name)
                else:
                    urllib.request.urlretrieve(image, picture_name)
            except (ValueError, urllib.error.URLError):
                pass
        print("Stahovanie dokoncene.")
    except :
        print("Chyba pri stahovani obrazkov.")

main()
