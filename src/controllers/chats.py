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

# Chat creation 



# Add username to the chat

@app.route("/chat/<chat_id>/adduser/<username>")
def adduser(chat_id,username):
  updatechat=collection.update({ "_id":ObjectId(chat_id) },{"$push": {"users":username}})
  updated=collection.find_one({'_id': ObjectId(chat_id)})
  return dumps(updated)


# Add message by username to the chat


@app.route("/chat/addmessage/<chat_id>/<username>/<text>")
def addMessage(chat_id,username,text):
  #query=collection.find_one({ "_id":ObjectId(chat_id)})
  #if username not in query:
  #  raise APIError("username not in the chat")
  #else:
  updatechat=collection.update({ "_id":ObjectId(chat_id) },{"$push": {"messages":text}})
  updated=collection.find_one({'_id': ObjectId(chat_id)},{messages:1})
  return dumps(updated)




 # - **Purpose:** Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
 # - **Params:**
 #   - `chat_id`: Chat to store message
 #   - `user_id`: the user that writes the message
 #   - `text`: Message text
 # - **Returns:** `message_id`