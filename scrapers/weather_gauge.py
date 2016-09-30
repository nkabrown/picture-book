import csv
import requests
from bs4 import BeautifulSoup

def get_weather(station_id):
    url = "http://w1.weather.gov/obhistory/" + station_id + ".html"
    r = requests.get(url)
    markdown = r.content
    soup = BeautifulSoup(markdown, "lxml")
    table_rows = soup.find_all("tr")
    table = table_rows[7:-5]
    list_of_rows = []
    for row in table:
        list_of_cells = []
        for cell in row.find_all("td"):
            text = cell.text
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

    with open("../temp/" + station_id + "_weather.csv", "wb") as csvfile:
        writer = csv.writer(csvfile)
        headers = ["date", "time(edt)", "wind(mph)", "vis(mi)", "weather", "sky_condition", "air_temp", "dewpoint_temp", "6_hour_max", "6_hour_min", "relative_humidity", "wind_chill", "heat_index", "alitimeter_pressure", "sea_level_pressure", "precip_one_hr", "precip_three_hr", "precip_six_hr"]
        writer.writerow(headers)
        writer.writerows(list_of_rows)

# 4 character noaa weather station id listed at http://forecast.weather.gov/stations.php
get_weather("KLGA")

