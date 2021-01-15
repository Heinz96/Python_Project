from flask import Blueprint, render_template, request, redirect, url_for
from extensions import *
from models.strategy import *

main = Blueprint("main", __name__)

#Landing route
@main.route("/")
def hello_world():
   return render_template("landing.html")

#Main page route
@main.route('/strategies', methods=["GET"])
def strategies_get():
	Strats = Strategy.objects
	return render_template("index.html", Strategies=Strats)

#Getting the post to create a new strategy 
@main.route('/strategies', methods=["POST"])
def strategies_post():
	Strategy(
	name = request.form["name"],
	image = request.form["image"],
	description = request.form["description"]).save()

	return redirect(url_for("main.strategies_get"))
   # return render_template("index.html")

#Showing the strategy
@main.route('/strategies/<_id>', methods=["GET"])
def strategies_ind(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("show.html",strat=strat)
	
#Template if there is the need to create a new strategy
@main.route('/strategies/new', methods=["GET"])
def strategies_new():
   return render_template("new.html")

#Edit route
@main.route('/strategies/<_id>/edit', methods=["GET"])
def strategies_edit(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("edit.html", strat=strat)

#Modifying the database
@main.route('/strategies/<_id>', methods=["POST"])
def strategies_update(_id=None):
	Strategy.objects(id=_id).update(
	name = request.form["name"],
	image = request.form["image"],
	description = request.form["description"])
	for strat in Strats:
		strat.reload()
	return redirect("/strategies/" + _id)

#Deleting a strategy
@main.route('/strategies/<_id>/delete', methods=["POST"])
def strategies_delete(_id=None):
	Strategy.objects(id=_id).delete()
	return redirect(url_for("main.strategies_get"))