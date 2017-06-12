import csv
from lxml import html
import requests

class scrapeISOCodes:
    def __init__(self):
        self.url = 'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'

    def scrape(self):
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        language_names = tree.xpath('//tr/td[position()=3]/a[position()=1]/text()')
        two_letter_codes = tree.xpath('//tr/td[position()=5]/text()')
        self.write_to_csv(language_names, two_letter_codes)

    def write_to_csv(self, names, codes):
        outfile = open('iso_639_1_codes.csv', 'wb')
        writer = csv.writer(outfile)
        writer.writerow(['language', 'code'])
        for i, name in enumerate(names):
            writer.writerow([name.encode('utf-8'), codes[i]])

scrapeISOCodes().scrape()
