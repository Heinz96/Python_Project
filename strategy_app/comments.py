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
	newComment = Comment(content=request.form["content"]).save()
	strat = Strategy.objects(id=_id).first()
	strat.comments.append(newComment)
	strat.save()
	for strat in Strats:
		strat.reload()
	return redirect("/strategies/" + _id)

@second.route("/<comment_id>/edit")
def comment_edit(_id=None, comment_id=None):
	comment = Comment.objects(id=comment_id).first()
	strat = Strategy.objects(id=_id).first()
	return render_template("comments/edit.html", Strat=strat, comment=comment)

@second.route("/<comment_id>", methods=["POST"])
def comment_update(_id=None, comment_id=None):
	Comment.objects(id=comment_id).update(content=request.form["content"])
	for strat in Strats:
		strat.reload()
	return redirect("/strategies/" + _id)

@second.route('/<comment_id>/delete', methods=["POST"])
def comment_delete(_id=None, comment_id=None):
	Comment.objects(id=comment_id).delete()
	return redirect("/strategies/" + _id)