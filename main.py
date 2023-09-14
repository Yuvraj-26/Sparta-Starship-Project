import json
import requests
import pymongo
from pymongo import response


# Need to get the Starships API from SWAPI


# 1) Method to get all urls that are for starships
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


#Importing to MongoDB from here:
def import_one_into_mongo(collection, ship):
    print(f"ship: {ship}")
    collection.insert_one(ship)


def import_all_into_mongo(collection, ships):
    for ship in ships:
        import_one_into_mongo(collection, ship)


#Create a method to create a JSON FILE -
def import_all_into_json_file(ships):
    with open("myship.json", "w") as f:
        json.dump(ships, f)

def write_pilots(data):
    with open("pilots.json", "w") as f:
        json.dump(data, f)



#Calling functions:
starships = fetch_starships()

outcome = {}
    for ship in starships:
        print(f"Ship: {ship['name']}")
        pilots = ship['pilots']
        if len(pilots) == 0:
            print(f"\tship {ship['name']} has no pilots")
        else:
            for pilot in pilots:
                print(f"\tpilot: {pilot}")
        outcome[ship['name']] = ship['pilots']

write_pilots(outcome)


print(f"found total of {len(starships)}")

# client = pymongo.MongoClient()
# db = client['starwars']
# shipsCollection = db["starships"]

# import_all_into_mongo(shipsCollection, starships)
import_all_into_json_file(starships)

fetch_starships()