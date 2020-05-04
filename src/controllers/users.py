from src.app import app
from src.config import *
from bson.json_util import dumps
import re
import json
from src.helpers.errorHandler import *
from bson.objectid import ObjectId
from flask import request,jsonify
import scipy.spatial.distance as distance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
from sklearn.pipeline import Pipeline



# Welcome to the API

@app.route("/")

def welcomeapi():
    res="Welcome to the chat sentiment analysis API. See this link to know how it works: https://github.com/soledb94/Chat_Sentiment_Analysis_Service/blob/master/README.md"
    return dumps(res)



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

    else:
        query2=collection.find({},{"messages":1,"_id":1})
  
        query2=[e for e in query2 if e]
        docs=[]

        m={}
        for e in docs:
            m={":".join("{}:{}".format(k,v) for k,v in e.items())}
        
        count_vectorizer = CountVectorizer()
        sparse_matrix = count_vectorizer.fit_transform(m)
        m = sparse_matrix.todense()

        doc_term_matrix = sparse_matrix.todense()
        df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=m.keys())


        similarity_matrix = distance(df,df)
        sim_df = pd.DataFrame(similarity_matrix, columns=docs.keys(), index=docs.keys())

        similatirities=sim_df[1:4]

        return dumps(similarities)


    
















