from flask import Flask, render_template, request, redirect, url_for
import random 
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from mongoengine import *



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
Bootstrap(app)
connect("myDatabase")

  
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

# call = Strategy(name="call", image="null", description="end").save()

Strats = Strategy.objects

@app.route('/')
def hello_world():
   return render_template("landing.html")

@app.route('/strategies', methods=["GET"])
def strategies_get():
	Strats = Strategy.objects
	return render_template("index.html", Strategies=Strats)

@app.route('/strategies', methods=["POST"])
def strategies_post():
	Strategy(
	name = request.form["name"],
	image = request.form["image"],
	description = request.form["description"]).save()

	return redirect(url_for("strategies_get"))
   # return render_template("index.html")

@app.route('/strategies/<_id>', methods=["GET"])
def strategies_ind(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("show.html",strat=strat)
	

@app.route('/strategies/new', methods=["GET"])
def strategies_new():
   return render_template("new.html")


@app.route('/strategies/<_id>/edit', methods=["GET"])
def strategies_edit(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("edit.html", strat=strat)

@app.route('/strategies/<_id>', methods=["POST"])
def strategies_update(_id=None):
	Strategy.objects(id=_id).update(
	name = request.form["name"],
	image = request.form["image"],
	description = request.form["description"])
	for strat in Strats:
		strat.reload()
	return redirect("/strategies/" + _id)

@app.route('/strategies/<_id>/delete', methods=["POST"])
def strategies_delete(_id=None):
	Strategy.objects(id=_id).delete()
	return redirect(url_for("strategies_get"))

if __name__ == '__main__':
   app.run(debug=True)
