import json
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


# Load JSON data
def load_json_file(file_path):
    """
    Load JSON data from a file and return it as a Python dict
    """
    with open(file_path, 'r') as file:
        return json.load(file)


# Find the character name based on the character URL
def find_character_name(character_url: str, character_dict=None, pilots=None) -> str:
    """
    Function to return the character name from the character URL, using the dictionary imported from JSON
    """
    character_name = pilots[character_url]
    return character_name


# Find the character ID in MongoDB based on the character name
def find_character_id(character_name: str) -> str:
    """
     Function to return the character ID using the character name
    """
    character_id = db.characters.find({"name": character_name}, {"_id": 1})
    return character_id


# Combine find_character_name and find_character_id to get the character's ID from its URL
def find_id_from_url(character_url: str) -> str:
    """
    Function to use the find_character_name and find_character_id functions, to return a character's ID from its URL
    """
    name = find_character_name(character_url)
    id = find_character_id(name)
    return id


# Replace character URLs in the starships collection with character IDs
def replace_character_url(starships=None):
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
        db.starships.update({starship}, {"$set": {"pilot": pilot_ids}})


# A name to id mapping
def character_name_to_id_mapping(characters_collection):  # rename mapping function
    """
    Function to create a mapping of character names to character IDs
    """
    character_name_to_id = {}
    for character in characters_collection.find():
        character_name_to_id[character['name']] = character['_id']
    return character_name_to_id


# update pilot names with ids
def update_pilots_with_ids(starship_data, characters_collection):
    """
    Function to update pilot data with character IDs
    """
    for starship in starship_data:
        pilot_ids = []
        for pilot_name in starship['pilots']:
            pilot_id_object = characters_collection.find_one({"name": pilot_name}, {"_id": 1})
            if pilot_id_object:
                pilot_ids.append(pilot_id_object['_id'])
        starship['pilots'] = pilot_ids


# update starships with pilot names
def update_starships_with_pilots(starship_data, pilot_data):
    """
    Functions to update starships data with pilot names
    """
    for starship in starship_data:
        starship_name = starship['name']
        pilots = pilot_data.get(starship_name, [])
        pilot_names = [pilot['name'] for pilot in pilots]
        starship['pilots'] = pilot_names


# Update starships collection with pilot ids
def update_starships_with_pilot_ids(starships_data, pilots_data):
    """
    Function to update starships data with pilot IDs
    """
    for starship in starships_data:
        starship['pilots'] = [pilot['id'] for pilot in pilots_data.get(starship['name'], [])]
    return starships_data


def update_starships_in_mongodb(starship_data, collection_name):
    """
    Function to update the starships collection in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['starwars']

    starships_collection = db[collection_name]

    for starship in starship_data:
        query = {"name": starship["name"]}
        starships_collection.update_one(query, {"$set": starship}, upsert=True)

    # Close the MongoDB connection
    client.close()
