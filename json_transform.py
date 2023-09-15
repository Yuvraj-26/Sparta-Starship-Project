import json
import http 
import requests

with open("C:/Users/marti/Documents/SpartaDocs/Git2_0/Git_Sparta_BaseDirectory/Mongo/pilots.json") as jsonfile:
    list_of_Ships = json.load(jsonfile)
list_of_sublist_of_pilot_links = list(list_of_Ships.values())

print(list_of_sublist_of_pilot_links)

list_of_pilot_links = []
for sublist_of_pilot_links in list_of_sublist_of_pilot_links: 
    for pilot_links in sublist_of_pilot_links: 
        list_of_pilot_links.append(pilot_links)


# Creating a dictionary with links to pilots as keys. Values set equal to none. 
link_to_name_dict = {}
for link in list_of_pilot_links:
    link_to_name_dict[link] = None 

print(link_to_name_dict)



# Loading names from api to a list
names_list = []

for link in list_of_pilot_links:
    info = requests.get(link)
    name = info.json()['name']
    names_list.append(name)

print(names_list)



# sets values from none to names retreived from the api 

for name in names_list: 
    for key, value in link_to_name_dict.items():
        if value is None:
            link_to_name_dict[key] = name 

print(link_to_name_dict)
