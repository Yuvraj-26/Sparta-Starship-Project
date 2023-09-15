import unittest
import pymongo
import json
from your_module import find_character_name, find_character_id, find_id_from_url


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
        TESTS DIRECT REPLACEMENT IN JSON
        """
        actual = function()['Millennium Falcon']
        expected = ["Chewbacca",
                    "Han Solo",
                    "Lando Calrissian",
                    "Nien Nunb"]
        self.assertEqual(actual, expected)

    def test_URL_pilot_dictionary(self):
        """
        Takes the "function" function and checks the URL corresponds to the right name in the dictionary
        TESTS DICTIONARY
        """
        actual = function()["https://swapi.dev/api/people/13/"]
        expected = "Chewbacca"
        self.assertEqual(actual, expected)


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
        character_id = find_id_from_url(character_url)  # what the function is called in our code

        self.assertEqual(character_id, expected_id)


if __name__ == '__main__':
    unittest.main()
