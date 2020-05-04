from src.app import app
import nltk
import nltk.data
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.config import *
from bson.json_util import dumps
import json
import pandas as pd
from src.helpers.errorHandler import *
from bson.objectid import ObjectId
from flask import request,jsonify
sia = SentimentIntensityAnalyzer()


# Chat creation

@app.route("/chat/create",methods=["POST"])
@errorHandler
def createChat():
    _json=request.json
    chat_name=_json["chat_name"]

    query=collection.find_one({"chat_name":chat_name})
    if query:
        raise APIError("chat already exists")

    else:
        
        id=collection.insert_one({"chat_name":chat_name,"messages":[],"users":[]}) 
        resp=jsonify("chat added successfuly") 

        return resp


# Add user to the chat


@app.route("/chat/adduser/<chat_id>/<username_id>")
@errorHandler
def adduser(chat_id,username_id):
    query=collection.find_one({ "_id":ObjectId(chat_id),"users":username_id})
    if query:
        raise APIError("username already exists in chat")


    else:
        updatechat=collection.update({ "_id":ObjectId(chat_id) },{"$push": {"users":username_id}})

        resp=jsonify("user added successfully to the chat") 
        resp.status_code=200

        return resp

  
# Add message by username to the chat


@app.route("/chat/addmessage/<chat_id>/<username_id>",methods=["PATCH"])
@errorHandler
def addMessage(chat_id,username_id):
    _chat_id=chat_id
    _username_id=username_id
    _json=request.json
    _text=_json["messages"]


    query=collection.find_one({ "_id":ObjectId(chat_id),"users":username_id})
    if not query:
        raise APIError("username doesn´t exist in chat")

    else:

        updatemessage=collection.update({ "_id":ObjectId(chat_id) },{"$push":{"messages":_text}})
        resp=jsonify("message added successfully to the chat") 

        return resp


# Get list of messages in a chat

@app.route("/chat/<chat_id>/list")
@errorHandler
def getlist(chat_id):
    query=list(collection.find({ "_id":ObjectId(chat_id)},{"messages":1}))
    if len(query)==0:
        raise APIError("list if empty")

    return jsonify(query[0]["messages"])


# Sentiment analysis from a chat

@app.route("/chat/<chat_id>/sentiment")
@errorHandler
def getsentiments(chat_id):
    query=list(collection.find({ "_id":ObjectId(chat_id)},{"messages":1}))
    if len(query)==0:
        raise APIError("chat is empty")
    
    for e in query[0]["messages"]:
        conclusion=sia.polarity_scores(e)
    
    return dumps(conclusion)












