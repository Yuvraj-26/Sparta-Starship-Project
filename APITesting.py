import unittest
import pymongo

def test_starship_api_request(starship_api):
    """
    Expecting a json input of the results from the starships api pull.
    Should be length 36 which is what is checked here.
    Also checks the length of the first index in the json.
    """
    assert len(starship_api) == 36
    assert len(starship_api[0]) == 18


def test_url_from_api(pilot_url):
    """
    Expects the input from the 5th star ship in the API(index 4, Millenium Falcon)
    """
    assert pilot_url[5][1] == ["https://swapi.dev/api/people/13/",
                               "https://swapi.dev/api/people/14/",
                               "https://swapi.dev/api/people/25/",
                               "https://swapi.dev/api/people/31/"]


def test_pilot_api_request(pilot_api):
    """
    Expects a json input from the pilot's api request.
    Checks the length of the character json and checks it has the name category
    Should be length 16
    """
    assert len(pilot_api) == 16
    assert pilot_api['name'] == 'Luke Skywalker'


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