# App flask
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def root():
    return "Microblog MongoDb/Flask Demo"


@app.route("/api/posts", methods=['GET'])
def list_posts():
    # Crea un’istanza del client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database (se non presente, allora è creato)
    db = client["microblog"]

    # Accedo ad una collezione (se non presente, allora è creata)
    posts = db["posts"]

    #items = posts.find({},{"_id":0})
    items = posts.find()
    post_list = []
    for item in items:
        item["_id"] = str(item["_id"])
        post_list.append(item)

    result = {"posts": post_list}
    return jsonify(result)

@app.route("/api/post/<id>", methods=['GET'])
def list_post_by_id(id):
    # Crea un’istanza del client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database (se non presente, allora è creato)
    db = client["microblog"]

    # Accedo ad una collezione (se non presente, allora è creata)
    posts = db["posts"]

    item = posts.find_one({"_id": ObjectId(id)})
    item["_id"] = str(item["_id"])
    result = {"post": item}
    return jsonify(result)

@app.route("/api/post", methods=['POST'])
def post_post():
    # Crea un’istanza del client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database (se non presente, allora è creato)
    db = client["microblog"]

    # Accedo ad una collezione (se non presente, allora è creata)
    posts = db["posts"]

    # Creo un post come dizionario
    post = {
        "text": request.form.get('text', ''),
        "author": request.form.get('author', ''),
        "tags": [],
        "date": datetime.utcnow()
    }

    # Inserisco il post nella collezione
    result = posts.insert_one(post)

    # Visualizza l’id univoco del documento
    return jsonify({"post": str(result.inserted_id)})
