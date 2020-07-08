from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
num_all = []
for line in tags:
    line = line.decode().strip()
    num_list = re.findall('[0-9]+', line)
    
    if len(num_list) >= 1:
        for i in range(len(num_list)):
            num = int(num_list[i])
            num_all.append(num)

print('Count:', len(num_all))
print('Sum:', sum(num_all))
