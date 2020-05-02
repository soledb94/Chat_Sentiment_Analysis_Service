import os
import dotenv
dotenv.load_dotenv()
from pymongo import MongoClient


PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")


dbName = "chats"
mongodbURL = f"mongodb://localhost/{dbName}"
print(mongodbURL)
client = MongoClient(mongodbURL)
db = client.get_database()

collection=db["chats"]