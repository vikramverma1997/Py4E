import xml.etree.ElementTree as ET

data = '''
<person>
<name>Vikram Singh</name>
<phone>8265973123</phone>
<email hide='yes'/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attribute:', tree.find('email').get('hide'))