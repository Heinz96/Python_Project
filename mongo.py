from flask import Flask, render_template, request, redirect, url_for
import random 
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from mongoengine import *



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/kangaroo"
mongo = PyMongo(app)
Bootstrap(app)
connect("kangaroo")

class Comment(EmbeddedDocument):
	content = StringField()

class Author(EmbeddedDocument):
	name = StringField()

class Strategy(Document):
	author = EmbeddedDocumentField(Author)
	name = StringField(required=True)
	image = StringField(required=False)
	description = StringField(required=False)
	comments = ListField(EmbeddedDocumentField(Comment))



@app.route('/')
def hello_world():
	enzo = Strategy(author=Author(name="Enzo"), name="call", image="don't know", description="great strat").save()
	return "<h1>Good Job!<h1>"

@app.route('/Enzo')
def hello_enzo():
	for user in Strategy.objects:
		print(user.author.name)
	return "<h1>Good Job 2!<h1>"


if __name__ == '__main__':
   app.run(debug=True)