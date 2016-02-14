import json
import urllib2

url1 = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=new%20york%20times&srlimit=50&sroffset=0"
data1 = json.load(urllib2.urlopen(url1))

url2 = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=new%20york%20times&srlimit=50&sroffset=50"
data2 = json.load(urllib2.urlopen(url2))

title1 = [search['title'] for search in data1['query']['search']]
title2 = [search['title'] for search in data2['query']['search']]
titles = title1 + title2

for idx, title in enumerate(titles):
    url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&indexpageids&rvprop=content&format=json&titles='
    data = json.load(urllib2.urlopen(url+urllib2.quote(title)))
    with open("data{0}.txt".format(idx), "w") as outputfile:
        json.dump(data['query']['pages'][data['query']['pageids'][0]]['revisions'][0]['*'], outputfile)