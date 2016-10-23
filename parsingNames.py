import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = raw_input('count:')
count = int(count)
position = raw_input('position:')
position = int(position)


while count > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position - 1].get('href',None)
    count = count - 1 
    
print url