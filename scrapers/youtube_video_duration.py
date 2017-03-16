import csv, json
import httplib2
import isodate
import datetime
from bs4 import BeautifulSoup

# get titles and video durations from a list of youtube video ids

# before running remove unknown #NAME? video ids from the input csv before processing
# add your youtube data api key and rename the input and output csv files

def get_title(soup):
	span = soup.find('span', class_='watch-title')
	if span == None:
		 return 'Not found'
	elif span['title']:
		title = span['title']
		return title

with open('input.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimitier=',')
	list_of_rows = []
	for row in reader:
		list_of_values = []
		if row[0] != 'video_id':
			video = row[0]
			h = httplib2.Http('.cache')
			(response, content) = h.request('https://www.googleapis.com/youtube/v3/videos?id=' + video + '&part=contentDetails&key=YOUTUBE_DATA_API_KEY', 'GET')
			result = json.loads(content)
			if len(result['items']) > 0:
				list_of_values.append(video)
				url = 'https://www.youtube.com/watch?v=' + video
				(response, content) = h.request(url, 'GET')
				html = content
				soup = BeautifulSoup(html, 'lxml')
				title = get_title(soup)
				list_of_values.append(title)
				duration = result['items'][0]['contentDetails']['duration']
				# Youtube video duration property is formated as an ISO 8061 Duration representation
				timedelta = isodate.parse_duration(duration)
				list_of_values.append(timedelta)

with open('output.csv', 'wb') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(['video_id', 'title', 'duration'])
	for row in list_of_rows:
		row[1] = row[1].encode('utf')
		writer.writerow(row)
