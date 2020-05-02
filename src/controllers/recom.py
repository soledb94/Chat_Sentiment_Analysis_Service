from src.app import app
from src.config import *
from bson.json_util import dumps
import re
import json
from src.helpers.errorHandler import *
from bson.objectid import ObjectId
from flask import request,jsonify
from sklearn.feature_extraction.text import CountVectorizer
import scipy.spatial.distance as distance



#user creation

@app.route("/r/users/create",methods=["POST"])
@errorHandler
def r1():
    _json=request.json
    _name=_json["name"]
    
    query=collection.find_one({"name":_name})
    if query:
        raise APIError("username already exists")

    else:
        id=collection.insert_one({"name":_name}) 
        resp=jsonify("user added successfuly") 

        return resp

@app.route("/user/<user_id>/recommend")
@errorHandler
def getrecommendation(user_id):
    query=list(collection.find({ "_id":ObjectId(user_id)},{"messages":1}))
    if len(query)==0:
        raise APIError("user doesnt exists")

    
    query2=list(collection.find({},{"messages":1,"_id":0}))
    m=[query2[0]["messages"] for query2[0] in query2]
  
    return  dumps(m)
   

"""

- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users

"""

