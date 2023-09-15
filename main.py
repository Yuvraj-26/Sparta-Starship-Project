
import json
from pymongo import MongoClient
from swapi import fetch_starships, write_into_json_file, all_pilot_names, fetch_names_for_pilots, pilots_for_starships


from mongodb import (
    load_json,
    update_starships_with_pilots,
    replace_pilot_names_with_ids,
    update_starships_collection,
)



def main():

    # Getting all starships from SW API
    data = fetch_starships()
    print(data)
    write_into_json_file("starships.json", data)

    # Downloads all starships data from above var, then returns keys: URL and values: pilot name
    pilots = fetch_names_for_pilots(pilots_for_starships(data))
    print(pilots)
    write_into_json_file("pilots.json", pilots)

    starship_data = load_json('starships.json')
    pilot_data = load_json('pilots.json')

    update_starships_with_pilots(starship_data, pilot_data)

    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection URL
    db = client['starwars']  # Use the existing "starwars" database
    characters_collection = db['characters']  # Use the name of your characters collection

    replace_pilot_names_with_ids(starship_data, characters_collection)

    update_starships_collection(starship_data, 'starships')

    # Close the MongoDB connection
    client.close()


if __name__ == "__main__":
    main()
 


