#!/usr/bin/python
import urllib.request, sys,subprocess

def main():
    url=sys.argv[1]
    content_file="file.txt"
    download(url,content_file)

def download(url,content_file):
    make_file(content_file)
    html=urllib.request.urlopen(url)
    read_page=html.read()
    f=open(content_file, "w")
    f.write(str(read_page))
    f.close()

def make_file(content_file):
    subprocess.call( ['touch', content_file ] )

main()
