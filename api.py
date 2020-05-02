from src.config import PORT
from src.app import app
import src.controllers.chats
import src.controllers.users
import src.controllers.prueba
import src.controllers.recom




app.run("0.0.0.0", PORT, debug=True)
