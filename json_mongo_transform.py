import json
import http 
import requests

with open("C:/Users/marti/Documents/SpartaDocs/Git2_0/Git_Sparta_BaseDirectory/Mongo/pilots.json") as jsonfile:
    list_of_Ships = json.load(jsonfile)
list_of_sublist_of_pilot_links = list(list_of_Ships.values())

#print(list_of_sublist_of_pilot_links)


# A list of links to pages that contain information about starship pilots. There are duplicates. 
list_of_pilot_links = []
for sublist_of_pilot_links in list_of_sublist_of_pilot_links: 
    for pilot_links in sublist_of_pilot_links: 
        list_of_pilot_links.append(pilot_links)

#print(list_of_pilot_links,'\n')


# Link Keys: a dictionary which contains a DISTINCT link to each pilot, in the form of a key (repeat links are removed)
link_keys = {}
for link in list_of_pilot_links:
    link_keys[link] = None 
#print(link_keys)
#print(len(link_keys))
link_list = list(link_keys.keys()) 

# Loading names from api to a list: names_list

names_list = []

for link in link_list:
    info = requests.get(link)
    name = info.json()['name']
    names_list.append(name)

print(names_list)

# A  note of the values that exist within names list following by the api call 
#names_list = ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb', 'Luke Skywalker', 'Biggs Darklighter', 'Wedge Antilles', 'Jek Tono Porkins', 'Darth Vader', 'Boba Fett', 'Arvel Crynyd', 'Anakin Skywalker', 'Padmé Amidala', 'Gregar Typho', 'Ric Olié', 'Darth Maul', 'Obi-Wan Kenobi', 'Plo Koon', 'Grievous']

print(len(names_list))

# The values from both name and link lists are added to the output dictionary(key:link, value:name)
link_name_dict = {}
for i in range(len(link_keys)):
    link_name_dict[link_list[i]]=names_list[i]

print(link_name_dict)