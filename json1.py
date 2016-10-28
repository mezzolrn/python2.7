import json
import urllib

total = 0

url = raw_input('url:')
data = urllib.urlopen(url).read()

info = json.loads(data)

for i in info['comments']:
  total = total + i['count']

print total
