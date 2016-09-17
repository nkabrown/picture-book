import re, json
import requests
import urllib
from bs4 import BeautifulSoup

def get_data(hashtag):
    global result
    url = "https://www.instagram.com/explore/tags/" + hashtag + "/" 
    r = requests.get(url)
    markdown = r.content
    soup = BeautifulSoup(markdown, "lxml")
    script_tag = soup.find("script", string=re.compile("window._sharedData"))
    shared_data = script_tag.string.partition("=")[-1].strip(";")
    result = json.loads(shared_data)
    return result 

def get_recent_images(page_data):
    tags = result["entry_data"]["TagPage"][0]["tag"]
    tag_images_list = tags["media"]["nodes"]
    for image in tag_images_list:
        user_id = image["owner"]["id"]
        image_url = image["display_src"]
        image_id = image["id"]
        urllib.urlretrieve(image_url, "../temp/" + user_id + "_" + image_id + ".jpg")

get_data("phenomenology")
get_recent_images(result)
