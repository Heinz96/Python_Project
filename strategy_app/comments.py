from flask import Blueprint, render_template, request, redirect, url_for
from .extensions import *
from .models.strategy import *

second = Blueprint("second", __name__)

@second.route("/new")
def comment_new(_id=None):
	strat = Strategy.objects(id=_id).first()
	return render_template("comments/new.html", Strat=strat)