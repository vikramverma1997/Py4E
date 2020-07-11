import xml.etree.ElementTree as ET

# xml data
data = '''
<stuff>
    <users>
        <user x='1'>
            <id>001</id>
            <name>User1</name>
        </user>
        <user x='2'>
            <id>002</id>
            <name>User2</name>
        </user>
    </users>
</stuff>'''

# xml parsing
tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Id:', item.find('id').text)
    print('Name:', item.find('name').text)
    print('User attribute:', item.get('x'))