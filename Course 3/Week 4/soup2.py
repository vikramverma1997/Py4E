import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count - ')
position = input('Enter position - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
href = []
for tag in tags:
     href_tag = tag.get('href', None)
     if href_tag is not None:
        href.append(href_tag)

for i in range(int(count) - 1):
    html_new = urllib.request.urlopen(href[int(position) - 1], context=ctx).read()
    soup_new = BeautifulSoup(html_new, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup_new('a')
    href = []
    for tag in tags:
        href_tag = tag.get('href', None)
        if href_tag is not None:
            href.append(href_tag)
    
link = href[int(position) - 1]
name = re.findall('known_by_(.+)', link)
print(name)
