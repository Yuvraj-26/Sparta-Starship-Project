import json
import requests
import pymongo
from ast import literal_eval

# Need to get the Starships API from SWAPI


# Creating a method
def get_starships_page(url):
    print("loading data from ", url)
    starships = requests.get(url)
    return starships.json()


def fetch_starships():
    next_page = "https://swapi.dev/api/starships/?page=1"
    result = []
    while next_page is not None:
        response = get_starships_page(next_page)
        print("retrieved results:", response)
        result.extend(response.get('results'))
        next_page = response["next"]
        print(f"calling next ships on page: {next_page}")
    return result


ships = fetch_starships()


print(f"found total of {len(ships)}")

for ship in ships:
    print(f"ship: {ship}")