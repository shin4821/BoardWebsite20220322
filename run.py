from main import app
import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9000)
    

#mongo client is connected
client = MongoClient()
db     = client['db']

