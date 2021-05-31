# Importo il namespace
from pymongo import MongoClient
from datetime import datetime

# Crea un’istanza del client
client = MongoClient("mongodb://localhost:27017/")


# Accede ad un database (se non presente, allora è creato)
db = client["microblog"]


# Accedo ad una collezione (se non presente, allora è creata)
posts = db["posts"]

# Creo un post come dizionario
post = {
    "text": "My first microblog post!",
    "author": "John",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.utcnow()
}

# Inserisco il post nella collezione
result = posts.insert_one(post)

# Visualizza l’id univoco del documento
print(result.inserted_id)
