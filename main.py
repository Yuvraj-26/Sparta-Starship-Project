from swapi import fetch_starships, write_into_json_file, all_pilot_names, fetch_names_for_pilots, pilots_for_starships

# Getting all starships from SW API
data = fetch_starships()
print(data)
write_into_json_file("starships.json", data)

# Downloads all starships, then for each pilot URL downloads the pilot data
# Groups pilots by starships
pilots = fetch_names_for_pilots(pilots_for_starships(data))
print(pilots)
write_into_json_file("pilots.json", pilots)