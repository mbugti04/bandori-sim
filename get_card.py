from urllib.request import urlopen
import json
link = 'http://bandori.party/api/cards/'
response = urlopen(link)
data = json.load(response.read())
print(data)