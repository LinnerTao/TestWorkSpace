import json
from urllib.request import urlopen
url = "http://v.youku.com/v_show/id_XMzU5OTUzNzM0NA==.html?spm=a2hzy.20009934.contentHolderUnit6.A"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.load(contents)
for video in data['feed']['entry'][0-6]:
    print(video['title']['$t'])
