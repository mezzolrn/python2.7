import urllib
import xml.etree.ElementTree as ET

sum = 0

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)
print tree




comment = tree.find('comments').findall('comment')


for i in comment:
    sum = sum + int(i.find('count').text)

print sum