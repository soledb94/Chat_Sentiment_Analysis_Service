# Chat_Sentiment_Analysis_Service

<p align="center">
  <img width="100" height="100" src=INPUT/labs.png?raw=true "Title">
</p>


Public API for a chat sentiment analysis => https://....herokuapp.com/


***

Para la **limpieza** del Dataset he realizado las siguientes técnicas:

- REDUCCIÓN DEL NÚMERO DE COLUMNAS A LAS QUE SON INTERESANTES PARA EL ESTUDIO
- COMPROBACIÓN DE VALORES NULOS EN LA COLUMNA "DATE" Y ELIMININACIÓN DE ESTOS
- PRIMER BARRIDO DE REGISTROS DUPLICADOS
- ESTUDIO DE VALORES NULOS A LO LARGO DEL DATAFRAME
- ELIMINACIÓN DE LA COLUMNA DE "LOCATION", YA QUE NO ES NECESARIA EN ADELANTE
- REDUCCIÓN DEL DATAFRAME A LAS ACTIVIDAD DE "SURFING" EN FLORIDA (USA)
- TRATAMIENTO DEL CAMPO "DATE", PARA EXTRAER LOS MESES 
- ELIMINACIÓN LA COLUMNA "DATE", YA QUE NO ES NECESARIA EN ADELANTE

***


## Chat endpoints

| HTTP Method 	| URI path      	| Description                                    	| 
|-------------	|---------------	|------------------------------------------------	|
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