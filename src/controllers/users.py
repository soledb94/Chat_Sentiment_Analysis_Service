from src.app import app
from src.config import *
from bson.json_util import dumps
import re
import json
from src.helpers.errorHandler import *
from bson.objectid import ObjectId
from flask import request,jsonify


#user creation

@app.route("/users/create",methods=["POST"])
@errorHandler
def createUsername():
    _json=request.json
    _name=_json["name"]
    
    query=collection.find_one({"name":_name})
    if query:
        raise APIError("username already exists")

    else:
        id=collection.insert_one({"name":_name}) 
        resp=jsonify("user added successfuly") 

        return resp


#user recommendation


@app.route("/user/<user_id>/recommend")
@errorHandler
def getrecommendation(user_id):
    query=list(collection.find({ "_id":ObjectId(user_id)},{"messages":1}))
    if len(query)==0:
        raise APIError("user doesnt exists")
















