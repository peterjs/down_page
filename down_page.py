#!/usr/bin/python
import urllib.request, sys

def main():
    url=sys.argv[1]
    content_file="page.html"
    download(url,content_file)

def download(url,content_file):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    try:
        src = page.read().decode('utf8')
    except UnicodeDecodeError:
        src = page.read()
    f=open(content_file, "w")
    f.write(str(src))
    f.close()

main()
