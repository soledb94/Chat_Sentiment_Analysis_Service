# Chat_Sentiment_Analysis_Service

<p align="center">
  <img width="100" height="100" src=INPUT/labs.png?raw=true "Title">
</p>


***



Public API for a chat sentiment analysis => https://chat-sentiment-analysis-serv.herokuapp.com/



***


## Chat endpoints

| HTTP Method 	| URI path      	| Description                                    	| 
|-------------	|---------------	|------------------------------------------------	|
| GET         	| /               | Welcome to the api.    |   
| POST         	| /chat/create         	| Chat creation         	| 
| GET         	| /chat/adduser/<chat_id>/<username_id> 	| Adding users to the chat
| PATCH        	| /chat/addmessage/<chat_id>/<username_id>	| Adding message by user to the chat    |
| GET         	| /chat/<chat_id>/list	| Getting a list of chat messages for a chat ID 	   |
| GET         	| /chat/<chat_id>/sentiment	| Sentiment analysis for a chat based in the chat messages   |   


## User endpoints



| HTTP Method 	| URI path      	| Description                                    	| 
|-------------	|---------------	|------------------------------------------------	|
| POST       	| /users/create           	| Adding user to the DB |    	
| GET         	| /user/<user_id>/recommend 	| Recommending users to have a chat according to users simmilarities| 