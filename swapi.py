import json
import requests

'''
- Creating a function to pull the data on all the starships into a JSON file
- 1st problem: When we pulled data originally and done a count on the starships
    it did not return the full count of 36.
    Resolved this by creating a sub function (fetch page) 
    which returns the URL of the next page. 
'''


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
        # The line above within the loop is gathering all data within the 'results' object
        next_page = response["next"]  # This line of code is retrieving URL for the next page
        print(f"calling next ships on page: {next_page}")  # This shows the URL
    return result


# Method 2 - To create a JSON FILE --------------------------------------------------------------------------------
def write_into_json_file(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f)


# Method 3 - Using the data from the API json file (function above) -------------------------------------
# Grouping all the ships with their pilots --------------------------------------------------------------
def pilots_for_starships(ships):
    outcome = []
    for ship in ships:
        print(f"Ship: {ship['name']}")
        pilots = ship['pilots']
        for pilot in pilots:
            outcome.append(pilot)
    return outcome


def fetch_pilots_for_starships():
    ships = fetch_starships()
    return pilots_for_starships(ships)


# Method 4 - Same as above, but using the data from the above function 'pilots_for_starships()'
# But, instead follows the url and loads the pilot name
# We only need a list of dictionaries as: Key = URL and Values = Pilot name
def fetch_names_for_pilots(pilot_urls):
    pilots = []
    for url in pilot_urls:
        print("loading data from ", url)
        pilot_info = requests.get(url).json()
        pilot = {
            url: pilot_info['name'] # Only want to return the key: URL value: name
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


def all_pilot_names(ships, ship_name=None):
    outcome = {}
    for ship in ships:
        if ship['name'] == ship_name or ship_name is None:
            pilots = fetch_names_for_pilots(ship['pilots']) # Sub function
            outcome.extend(pilots)
            # iterates over the specified iterable and appends its elements to the end of the current list
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
    return list(map(pilot_name, pilots))  # Using the list and map functions to follow TDD


# Downloads all the ships and pilots - Groups them by ship and gives URL and name for each pilot
def fetch_all_pilot_names_for_starships():
    ships = fetch_starships()
    temp = pilot_names_for_starships(ships)
    return temp
