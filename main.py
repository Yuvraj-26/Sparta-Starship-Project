from mongo import SwapiMongo
from swapi import fetch_starships, write_into_json_file, fetch_all_pilot_names_for_starships


# Getting all starships from SW API
data = fetch_starships()
write_into_json_file("starships.json", data)


# Downloads all starships, then for each pilot URL downloads the pilot data
# Groups pilots by starships
pilots = fetch_all_pilot_names_for_starships()
write_into_json_file("pilots.json", pilots)


# mongo = SwapiMongo()
# mongo.import_one_into_mongo()
