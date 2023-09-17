import json
from pymongo import MongoClient

from mongodb import (
    load_json_file,
    find_character_name,
    find_character_id,
    find_id_from_url,
    replace_character_url,
    character_name_to_id_mapping,
    update_pilots_with_ids,
    update_starships_with_pilots,
    update_starships_with_pilot_ids,
    update_starships_in_mongodb

)


def main():
    try:
        starship_data = load_json_file('starships.json')
        pilot_data = load_json_file('pilots.json')

        update_starships_with_pilots(starship_data, pilot_data)

        client = MongoClient('mongodb://localhost:27017/')  # our MongoDB collection
        db = client['starwars']  # Use the existing starwars database
        characters_collection = db['characters']  # characters collection

        update_pilots_with_ids(starship_data, characters_collection)

        update_starships_in_mongodb(starship_data, 'starships')

        # Close the MongoDB connection
        client.close()

        print("Code ran successfully.")
        print("Pilot URLs have been updated to Character IDs.")
        print("Please view your mongodb starwars.starships collection.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
