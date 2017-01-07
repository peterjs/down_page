#!/usr/bin/python
import urllib.request, sys

def main():
    try:
        url=sys.argv[1]
    except IndexError:
        print("""Zla syntax! Spravna: python3 down_page.py "http://www.blahblah.com" """)
        sys.exit()
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
