from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
import json
from src.helpers.errorHandler import *
from bson.objectid import ObjectId



@app.route("/users/create/<username>")
@errorHandler
def createUsername(username):
#  query=collection.find_one({"username":username})
#  print(query)
#  if len(list(query))>0:
#    raise APIError("username already exists")
#  else:
    user={"username":username}
    newuser=collection.insert_one(user).inserted_id
    return dumps(newuser)