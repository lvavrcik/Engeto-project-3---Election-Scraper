import os
import sys
import csv
import requests
from bs4 import BeautifulSoup as BS
from typing import List

CHECK = "https://www.volby.cz/pls/ps2017nss/ps32"

try:
    FILE_NAME = sys.argv[2]
except IndexError:
    print("Filename not specified.")
    sys.exit()
else:
    if ".csv" not in FILE_NAME:
        print("Wrong file format entered.")
        sys.exit()
    elif os.path.exists(FILE_NAME):
        print("Entered file name '{}' already exists".format(FILE_NAME))
        sys.exit()

try:
    URL = sys.argv[1]
except IndexError:
    print("URL not specified.")
    sys.exit()
else:
    if CHECK not in URL:
        print("Wrong URL entered.")
        sys.exit()


def main():

    print("CONNECTING to: {}".format(URL))
    req = get_response(URL)
    print("DOWNLOADING DATA from: {}".format(URL))

    parsed = make_soup(req)

    links = [n_link(URL, [a["href"]]) for a in get_links(parsed, "td.cislo a")]
    rows = [row(link) for link in links]

    print("SAVING DATA to: {}".format(os.path.abspath(FILE_NAME)))
    print_to_csv(rows, FILE_NAME, rows[0])


def get_response(url):
    try:
        with requests.session() as s:
            req = s.get(url)
    except ConnectionError:
        print("No response")
        sys.exit()
    else:
        return req


def make_soup(req):
    return BS(req.text, "html.parser")


def n_link(url, cast) -> str:
    old_url = url.split("/")[:-1]
    new_url = old_url + cast
    return "/".join(new_url)


def get_links(soup, selector) -> list:
    data = soup.select(selector)
    return data


def row(link) -> dict:
    req = get_response(link)
    parsed = make_soup(req)
    data = get_data(link, parsed)
    return data


def get_data(link, parsed) -> dict:
    data = {
          "Code": link.split("=")[-2].split("&")[0],
          "City": get_city_name(parsed),
          "Registered": parsed.find("td", {"headers": "sa2"}).text,
          "Envelopes": parsed.find("td", {"headers": "sa3"}).text,
          "Valid": parsed.find("td", {"headers": "sa6"}).text
         }
    data.update(find_candidate_parties(parsed))
    final_data = final(data)
    return final_data


def final(data: dict) -> dict:
    symbol = "\xa0"
    for key in data:
        value = data.get(key)
        if symbol in value:
            data[key] = value.split(symbol)[0]+value.split(symbol)[1]
    return data


def find_candidate_parties(parsed) -> dict:
    parties = {}
    for tables in parsed.find_all("table")[1:]:
        for key in tables.select("td.overflow_name"):
            parties.setdefault(key.text, key.find_next_sibling("td").text)
    return parties


def get_city_name(parsed) -> str:
    city = parsed.select("h3")
    for t in city:
        if "obec" in t.text.casefold():
            return t.text.strip("\n").split(": ")[-1]


def print_to_csv(data: List[dict], name, zahlavi) -> None:
    with open(name, "w", newline="", encoding= "UTF-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=zahlavi.keys())
        csv_writer.writeheader()
        for r in data:
            csv_writer.writerow(r)
    return None


if __name__ == "__main__":
    main()