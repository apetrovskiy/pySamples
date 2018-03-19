import json
from urllib.request import urlopen

url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
#url = "https://www.googleapis.com/youtube/v3/videos?alt=json"
url = "https://www.googleapis.com/youtube/v3/videos?part=1"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
