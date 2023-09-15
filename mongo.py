import pymongo


class SwapiMongo:
    def __init__(self):
        client = pymongo.MongoClient()
        db = client['starwars']
        self.__collection = db['starships']

    def import_one_into_mongo(self, ship):
        print(f"ship: {ship}")
        self.__collection.insert_one(ship)

    def import_all_into_mongo(self, ships):
        for ship in ships:
            self.import_one_into_mongo(ship)