from flask import Blueprint, render_template, request, redirect, url_for
from .extensions import *
from .models.strategy import *

second = Blueprint("second", __name__)

@second.route("/new")
def comment_new(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("comments/new.html", Strat=strat)

@second.route("", methods=["POST"])
def comment_post(_id=None):
	newComment = Comment(content=request.form["content"])
	strat = Strategy.objects(id=_id).first()
	strat.comments.append(newComment)
	strat.save()
	for strat in Strats:
		strat.reload()
	return redirect("/strategies/" + _id)