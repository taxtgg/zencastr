from zencastr.database import client, db
import pymongo.errors as errors

def test_db_connection():
	try:
		error = None
		db.count_documents({})
	except errors.ConnectionFailure:
		error = "ConnectionFailure"
	finally:
		assert error == None

