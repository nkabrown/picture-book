import re, json
import requests
import urllib
from bs4 import BeautifulSoup

def get_data(handle):
    global result
    url = "https://www.instagram.com/" + handle + "/"
    r = requests.get(url)
    markup = r.content
    soup = BeautifulSoup(markup, "lxml")
    script_tag = soup.find("script", string=re.compile("window._sharedData"))
    shared_data = script_tag.string.partition("=")[-1].strip(";")
    result = json.loads(shared_data)
    return result

def get_images(page_data):
    user = page_data["entry_data"]["ProfilePage"][0]["user"]
    user_id = user["id"]
    image_list = user["media"]["nodes"]
    for i, item in enumerate(image_list):
        image = item["display_src"]
        urllib.urlretrieve(image, "../temp/" + user_id + "_000" + str(i) + ".jpg")

get_data("manrepeller")
get_images(result)
