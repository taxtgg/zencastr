import pymongo
import config

DATABASE_NAME = "castr"
COLLECTION_NAME = "podcasts"

client = pymongo.MongoClient(config.MONGO_HOST, config.MONGO_PORT)

db = client[DATABASE_NAME][COLLECTION_NAME]
