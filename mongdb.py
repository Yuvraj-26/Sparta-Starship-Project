'''
- read the json file
- takes pilot url out of starship_data
- which character matches URL from dict
- pull ID for character
- swap URL for ID in starship_data
- create collection in DB
- loading data into DB


- pull the relevant IDs from the DB
- edit the starship data to change the urls for the IDs

got characters (need to pull starship data, & API search to get 
character name from URL in starship object)

2 JSON files: 1 with all starship data & another dict with key/value 
pairs for URL & character name

'''

import json
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def read_json_file(data_set):
    """
    Function to read each json file so that we can use the data
    """
    try: 
        with open ('file.json', 'r' ) as json_file:
            data_set = json.load(json_file)
            return data_set
    except: 
        FileNotFoundError: print("File not found.")



def create_starship_collection():
    """
    Function to create & populate a collection for the starships
    """
    db.create_collection("starships")
    for starship in starship_data:
        db.starships.insert_one(starship)


def find_character_name(character_url: str) -> str:
    """
    Function to return the character name from the character url, using the dictionary imported from json
    """
    # character_name = character_dict.get(character_url)
    character_name = character_dict[character_url]
    return character_name


def find_character_id(character_name: str) -> str:
    """
    Function to return the character ID from the MongoDB using the character name
    """
    character_id = db.characters.find({"name": character_name}, {"_id":1})
    return character_id


def find_id_from_url(character_url: str) -> str:
    """
    Function combining the find_character_name & find_character_id functions, to return a character's ID from its URL
    """
    name = find_character_name(character_url)
    id = find_character_id(name)
    return id


def replace_character_url():
    """
    Function to loop through the objects in the starship collection, replacing the list associated with the 'Pilot' key
    with a new list of the character IDs, generated using our find_id_from_url function
    """
    for starship in db.starships: 

        pilot_urls = []
        pilot_ids = []
        for pilot_url in starships.pilot: 
            pilot_urls.append(pilot_url)

            id = find_id_from_url(pilot_url)
            pilot_ids.append(id)
        
        db.starships.update({starship}, {"$set":{"pilot": pilot_ids}})

