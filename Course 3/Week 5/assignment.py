from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input('Enter location: ')
xml = urlopen(url).read()
data = xml.decode()
print('Retrieving', url)
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
count_no = tree.findall('.//count')
print('Count:', len(count_no))

sum = 0
for item in count_no:
    number = int(item.text)
    sum += number

print('Sum:', sum)