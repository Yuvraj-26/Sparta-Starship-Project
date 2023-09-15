import json
import requests


# Method 1 - Call upon the SWAPI --------------------------------------------------------------------------------
# A method to call upon the swapi
def fetch_page(url):
    print("loading data from ", url)
    page = requests.get(url)
    return page.json()


# Looping through the pages of data (using a while loop)
# Loop until the link to the next page is 'null'
def fetch_starships():
    next_page = "https://swapi.dev/api/starships/?page=1"
    result = []
    while next_page is not None:
        response = fetch_page(next_page)
        print("retrieved results:", response)
        result.extend(response.get('results'))
        next_page = response["next"]
        print(f"calling next ships on page: {next_page}")
    return result


# Method 2 - Call upon the SWAPI --------------------------------------------------------------------------------
# To create a JSON FILE
def write_into_json_file(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f)


# Method 3 - Grouping all the ships with their pilots
def pilots_for_starships(ships):
    outcome = {}
    for ship in ships:
        print(f"Ship: {ship['name']}")
        pilots = ship['pilots']
        if len(pilots) == 0:
            print(f"\tship {ship['name']} has no pilots")
        else:
            for pilot in pilots:
                print(f"\tpilot: {pilot}")
        outcome[ship['name']] = ship['pilots']
    return outcome


def fetch_pilots_for_starships():
    ships = fetch_starships()
    return pilots_for_starships(ships)


# Method 4 - Same as above, but follows the url and loads the pilot details (because we need the name)
def fetch_names_for_pilots(pilot_urls):
    pilots = []
    for url in pilot_urls:
        print("loading data from ", url)
        pilot_info = requests.get(url).json()
        pilot = {
            "url": url,
            "name": pilot_info['name']
        }
        pilots.append(pilot)
    return pilots


def pilot_names_for_starships(ships, ship_name=None):
    outcome = {}
    for ship in ships:
        if ship['name'] == ship_name or ship_name is None:
            pilots = fetch_names_for_pilots(ship['pilots'])
            outcome[ship['name']] = pilots
        else:
            print(f"skipping ship {ship['name']}")
    return outcome


# Method 5 -------------------------------------------------------------------------------
def pilot_name(pilot):
    return pilot['name']


# For the test - filter to search for 1 ship name
def fetch_pilot_names_for_starship(starship_name):
    ships = fetch_starships()
    pilots = pilot_names_for_starships(ships, starship_name)[starship_name]
    return list(map(pilot_name, pilots)) # Using the list and map functions to follow TDD


# Downloads all the ships and pilots - Groups them by ship and gives URL and name for each pilot
def fetch_all_pilot_names_for_starships():
    ships = fetch_starships()
    temp = pilot_names_for_starships(ships)
    return temp
