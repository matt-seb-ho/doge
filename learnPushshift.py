import pandas as pd
import datetime
import requests
import json
import csv

"""
# datetime
now = datetime.datetime.now()
print('datetime(auto): ', now)
print('unix time/epoch value: ', now.timestamp())

# http requests
url = 'https://api.github.com'
response1 = requests.get(url)
print('response: ', response1) 
"""

# pushshift request
def addUrlParam(url, name, val):
	if not val:
		url += ('&' + name + '=' + val)
	return url

def buildURL(after = None, before = None, search = None, sub = None):
	url = 'https://api.pushshift.io/reddit/search/submission/?'
	params = {'after':after, 'before':before, 'search':search, 'subreddit':sub}
	firstParam = True
	for name in params:
		if params[name] is not None:
			# if not firstParam:
			if firstParam:
				firstParam = False
			else:
				url += '&'
			url += (name + '=' + str(params[name]))
	return url

def getPosts(after = None, before = None, search = None, sub = None):
	# return None
	url = buildURL(after, before, search, sub)
	print('url: ', url)
	r = requests.get(url)
	data = json.loads(r.text)
	return data['data']

# print(buildURL(after = datetime.datetime.now().timestamp(), sub = 'dogecoin'))
# print(getPosts(after = '1d', sub = 'dogecoin'))
prevHour = getPosts(after = '1h', sub = 'dogecoin')
print('len: ', len(prevHour))
print('item0: ', prevHour[0])

