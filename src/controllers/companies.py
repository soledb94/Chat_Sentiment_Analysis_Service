from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
import json
from src.helpers.errorHandler import *
from bson.objectid import ObjectId



dbName = "chats"
mongodbURL = f"mongodb://localhost/{dbName}"
print(mongodbURL)
client = MongoClient(mongodbURL)
db = client.get_database()

collection=db["chats"]

@app.route("/chat/create/<chatname>")
def createChat(chatname):
 # query=collection.find_one({"chat_name":chatname},{"_id":0})
 # if len(list(query))>0:
 #   raise APIError("chat name already exists")
 # else:
  data={"chat_name":chatname,"messages":[],"users":[]}
  newchat=collection.insert_one(data)
  return dumps(newchat.inserted_id)


  



