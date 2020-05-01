
 


"""

- (GET) `/chat/<chat_id>/adduser`
  - **Purpose:** Add a user to a chat, this is optional just in case you want to add more users to a chat after it's creation.
  - **Params:** `user_id`
  - **Returns:** `chat_id`
- (POST) `/chat/<chat_id>/addmessage`
  - **Purpose:** Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
  - **Params:**
    - `chat_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<chat_id>/list`
  - **Purpose:** Get all messages from `chat_id`
  - **Returns:** json array with all messages from this `chat_id`
- (GET) `/chat/<chat_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat














 
#@app.route("/users/create/<username>")
#def createUsername():
#query=list(db.find({"username":f"{username}"})
  #={"username":f"{username}"}
  #=db.insert_one({"username":f"{username}"})
#  return dumps(db.insert_one({"username":f"{username}"}.insertered_id)

  #  content = request.get_json()
  #  print (content)
  #  return 'JSON posted'



# Funciones para insertar datos
#def insertDatosNotebook(NBDataconFecha) :

 #   insertNotebook = collection.insert(NBDataconFecha)




#@app.route("/")
#def hello():
#        return "First Flask APP"

#@app.route('/postjson', methods = ['POST'])
#def postJsonHandler():

 #   NBData = request.get_json()
    # Registro la fecha desde el lado del servidor
  #  NBData.update({"DATETIME":datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    # Inserto el valor en la base
   # insertDatosNotebook(NBData)
    #return 'JSON posted'




    
#def getCompany(name):
#    statement = db.find_one({"name":namereg},{"_id":0, "name":1, "home_url":1, "email_address":1})
#    namereg = re.compile(f"^{name}", re.IGNORECASE)

#    print(namereg)
#    if not company:
#        print("ERROR")
#        raise Error404("company not found")
#    print("OK")
##    return dumps(company)