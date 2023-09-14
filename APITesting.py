import unittest
import pymongo
import json


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
        actual = function()['Millennium Falcon']
        expected = ["https://swapi.dev/api/people/13/",
                    "https://swapi.dev/api/people/14/",
                    "https://swapi.dev/api/people/25/",
                    "https://swapi.dev/api/people/31/"]
        self.assertEqual(actual, expected)

    def test_pilot_api_request(self):
        """
        Takes the "function" function and checks the URLs have been replaces by character names
        """
        actual = function()['Millennium Falcon']
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


import unittest
from your_module import find_character_name, find_character_id, find_id_from_url

# Replace with your actual character_dict and db configurations for testing
character_dict = {
    "url1": "Character 1",
    "url2": "Character 2",
}


#### from Ruths
class TestCharacterFunctions(unittest.TestCase):

    def test_find_character_name(self):
        character_url = "url1"
        expected_name = "Character 1"

        character_name = find_character_name(character_url)

        self.assertEqual(character_name, expected_name)

    def test_find_character_id(self):
        character_name = "Character 1"

        mock_db = {
            "characters": [
                {"name": "Character 1", "_id": "mock_id_1"},
                {"name": "Character 2", "_id": "mock_id_2"},
            ]
        }

        # function name from our code
        character_id = find_character_id(character_name)

        self.assertEqual(character_id, {"_id": "mock_id_1"})

    def test_find_id_from_url(self):
        character_url = "url1"

        mock_db = {
            "characters": [
                {"name": "Character 1", "_id": "mock_id_1"},
                {"name": "Character 2", "_id": "mock_id_2"},
            ]
        }
        expected_id = {"_id": "mock_id_1"}
        character_id = find_id_from_url(character_url)  # what the function is called in pur cpde

        self.assertEqual(character_id, expected_id)


if __name__ == '__main__':
    unittest.main()