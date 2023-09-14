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
    try: 
        with open ('file.json', 'r' ) as json_file:
            data_set = json.load(json_file)
            return data_set
    except: 
        FileNotFoundError: print("File not found.")

def create_starship_collection():



def find_character_name(character_url):
    # character_name = character_dict.get(character_url)
    character_name = character_dict[character_url]
    return character_name


def find_character_id(character_name):
    character_id = db.characters.find({"name": character_name}, {"_id":1})
    return character_id


def find_id_from_url(character_url):
    name = find_character_name(character_url)
    id = find_character_id(name)
    return id


def replace_character_url():
    for starship in starships: 
        for pilot in starship.pilot: 
            id = find_id_from_url(pilot)
            p