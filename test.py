import unittest
import pymongo
import json
from swapi import fetch_starships, fetch_pilots_for_starships, fetch_pilot_names_for_starship

class Tests(unittest.TestCase):
    def test_starship_api_request(self):
        """
        Takes the "fetch_starships" function and checks the length of both the json and the objects in the json
        """
        actual_len = len(fetch_starships())
        actual_len_firstdata = len(fetch_starships()[0])
        expected1 = 36
        expected2 = 18
        self.assertEqual(actual_len, expected1)
        self.assertEqual(actual_len_firstdata, expected2)

    def test_url_from_api(self):
        """
        Takes the "function" function and checks the pilots are displayed as URLs
        """
        actual = fetch_pilots_for_starships()['Millennium Falcon']
        expected = ["https://swapi.dev/api/people/13/",
                    "https://swapi.dev/api/people/14/",
                    "https://swapi.dev/api/people/25/",
                    "https://swapi.dev/api/people/31/"]
        self.assertEqual(actual, expected)

    def test_pilot_api_request(self):
        """
        Takes the "function" function and checks the URLs have been replaces by character names
        """
        actual = fetch_pilot_names_for_starship('Millennium Falcon')
        expected = ["Chewbacca",
                    "Han Solo",
                    "Lando Calrissian",
                    "Nien Nunb"]
        self.assertEqual(actual, expected)


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
characters_collection = db["characters"]


def test_match_pilot_with_character():
    # Create a mock character in the characters collection
    characters_collection.insert_one({"name": "Luke Skywalker", "_id": "mock_id"})

    # Test matching a pilot's name with a character in the collection
    pilot_name = "Luke Skywalker"
    character = match_pilot_with_character(pilot_name, characters_collection)
    assert character is not None
    assert character["_id"] == "mock_id"


def test_change_pilot_url_to_object_id():
    # Create a mock character in the characters collection
    characters_collection.insert_one({"name": "Pilot 1", "_id": "mock_id"})

    # Test changing a pilot's URL to an Object ID
    pilot_url = "https://example.com/pilots/1"
    object_id = change_pilot_url_to_object_id(pilot_url, characters_collection)
    assert object_id is not None
    assert object_id == "mock_id"


def test_import_all_into_mongo(self, mock_mongo_client):
    # Mock MongoDB client and collection
    mock_db = mock_mongo_client.return_value
    mock_collection = mock_db['test_collection']

    # Create sample ships
    sample_ships = [{"name": "Ship 1"}, {"name": "Ship 2"}]

    # Call the function to import all ships into MongoDB
    import_all_into_mongo(mock_collection, sample_ships)

    # Assertions
    mock_collection.insert_many.assert_called_once_with(sample_ships)


if __name__ == '__main__':
    unittest.main()