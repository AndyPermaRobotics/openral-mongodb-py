
import pytest
from pymongo import MongoClient
from pymongo.database import Database

from openral_mongodb_py import RalRepositoryMongoDB


class TestRalRepositoryMongoDB:
    """
    IMPORTANT: Tests the RalRepositoryMongoDB class with a real MongoDB instance.

    You can start a MongoDB instance with the dockercompose file in tests/assets/docker-compose.yml:
    $> docker-compose -p=openral_mongodb_py -f tests/assets/docker-compose.yml up -d
    
    """

    client_connection_str = "mongodb://localhost:27017/"
    database_name = "openral_mongodb_py_test"
    collection_name = "ral_objects"

    @pytest.fixture
    def connect_to_mongodb(self) -> RalRepositoryMongoDB:
        """
        Connects to a MongoDB instance and returns the database.
        """

        client = MongoClient(TestRalRepositoryMongoDB.client_connection_str)

        database : Database = client[TestRalRepositoryMongoDB.database_name]

        collection = database.create_collection(TestRalRepositoryMongoDB.collection_name)

        collection.insert_many([

        ])


        repository = RalRepositoryMongoDB(database, TestRalRepositoryMongoDB.collection_name)

        return repository

    def test_get_ral_object_by_uid(self, connect_to_mongodb : RalRepositoryMongoDB):
        """
        Tests the get_ral_object_by_uid() method.
        """


        #TODO

        assert False, "TODO"