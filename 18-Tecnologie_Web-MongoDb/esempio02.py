# Importo il namespace
from pymongo import MongoClient
from datetime import datetime

# Crea un’istanza del client
client = MongoClient("mongodb://localhost:27017/")


# Accede ad un database (se non presente, allora è creato)
db = client["microblog"]


# Accedo ad una collezione (se non presente, allora è creata)
posts = db["posts"]

# Recupera i post presenti nella collezione
result = posts.find()

# Visualizza i post
for item in result:
    print(item)
