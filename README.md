# Chat_Sentiment_Analysis_Service

Public API for a chat sentiment analysis => https://....herokuapp.com/


## Chats endpoints

| HTTP Method 	| URI path      	| Description                                    	| 
|-------------	|---------------	|------------------------------------------------	|
| POST         	| /chat/create         	| Chat creation         	| 
| GET         	| /chat/adduser/<chat_id>/<username_id> 	| Adding users to the chat
| PATCH        	| /chat/addmessage/<chat_id>/<username_id>	| Adding message by user to the chat    |
| GET         	| /chat/<chat_id>/list	| Getting a list of chat messages for a chat ID 	   |
| GET         	| /chat/<chat_id>/sentiment	| Sentiment analysis for a chat baed in the chat messages   |   


## Users endpoints



| HTTP Method 	| URI path      	| Description                                    	| 
|-------------	|---------------	|------------------------------------------------	|
| POST       	| /users/create           	| Adding user to the DB |    	
| GET         	| /user/<user_id>/recommend 	| Recommending users to chat according to users simmilarities| 