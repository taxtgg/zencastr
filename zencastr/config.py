import os

DEPLOYMENT_ENV = os.environ.get('ENV', 'dev')

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', '27017'))
