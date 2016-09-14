import re, json
import requests
import urllib
from bs4 import BeautifulSoup

def getImages(username):
    url = "https://www.instagram.com/" + username + "/"
    r = requests.get(url)
    markup = r.content
    soup = BeautifulSoup(markup, 'lxml')
    script_tag = soup.find('script', string=re.compile('window._sharedData'))
    shared_data = script_tag.string.partition('=')[-1].strip(';')
    result = json.loads(shared_data)
    user = result["entry_data"]["ProfilePage"][0]
    ID = user["user"]["id"]
    image_list = user["user"]["media"]["nodes"]
    for i, item in enumerate(image_list):
        image = item["display_src"]
        urllib.urlretrieve(image, '../images/' + ID + '_000' + str(i) + '.jpg') 

getImages("manrepeller")
