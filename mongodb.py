import json
from pymongo import MongoClient
import pymongo


client = pymongo.MongoClient()
db = client['starwars']
 

# Load JSON data
def load_json_file(file_path):
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

 

def character_name_to_id_mapping(characters_collection): # rename mapping function
    """
    Function to create a mapping of character names to character IDs
    """
    character_name_to_id = {}
    for character in characters_collection.find():
        character_name_to_id[character['name']] = character['_id']
    return character_name_to_id

 

def update_pilots_with_ids(pilots_data, character_name_to_id):
    updated_pilots_data = {}
    for starship_name, pilots in pilots_data.items():
        updated_pilots = []
        for pilot in pilots:
            character_name = pilot['name']
            character_id = character_name_to_id.get(character_name)
            if character_id:
                updated_pilot = {
                    'id': character_id,
                    'name': character_name
                }
                updated_pilots.append(updated_pilot)
        updated_pilots_data[starship_name] = updated_pilots
    return updated_pilots_data

 

def update_starships_with_pilot_ids(starships_data, pilots_data):
    for starship in starships_data:
        starship['pilots'] = [pilot['id'] for pilot in pilots_data.get(starship['name'], [])]
    return starships_data

 

def update_starships_in_mongodb(updated_starships_data, db_name='starwars', mongodb_url='mongodb://localhost:27017/'):
    client = MongoClient(mongodb_url)
    db = client[db_name]
    starships_collection = db['starships']
    for starship in updated_starships_data:
        starships_collection.update_one({'name': starship['name']}, {'$set': {'pilots': starship['pilots']}})
    client.close()

 