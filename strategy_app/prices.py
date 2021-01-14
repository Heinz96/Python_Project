from flask import Blueprint, render_template, request, redirect, url_for
from extensions import *
from models.strategy import *
from pricing.Black_Scholes import *
from pricing.autocall import *

third = Blueprint("third", __name__)

# @third.route("/new")
# def comment_new(_id=None):
# 	strat = Strategy.objects(id=_id).first()
# 	return render_template("comments/new.html", Strat=strat)

@third.route("", methods=["POST"])
def price_post(_id=None):
    Option=request.form["Option"]
    S=float(request.form["S"])
    K=float(request.form["K"])
    r=float(request.form["r"])/100
    sigma=float(request.form["sigma"])/100
    t=float(request.form["t"])

    if Option=="Call":
        C = call(S, K, sigma, r, t)
        newPrice = Price(Option=Option,S=S,K=K,r=r,sigma=sigma,t=t,C=C).save()
    elif Option =="Put":
        C = put(S, K, sigma, r, t)
        newPrice = Price(Option=Option,S=S,K=K,r=r,sigma=sigma,t=t,C=C).save()
    elif Option=="Autocall":
        Coupon=float(request.form["Coupon"])
        Barrier=float(request.form["Barrier"])
        C = autocall_pricing(np, 10**6, r, sigma, t, S, K, Coupon, Barrier)
        newPrice = Price(Option=Option,S=S,K=K,r=r,sigma=sigma,t=t,C=C,Coupon=Coupon,Barrier=Barrier).save()

    strat = Strategy.objects(id=_id).first()
    strat.prices.append(newPrice)
    strat.save()
    for strat in Strats:
        strat.reload()
    
    print(S, K, r, sigma, t, C, Option, Coupon, Barrier)
    return redirect("/strategies/" + _id)

# @second.route("/<comment_id>/edit")
# def comment_edit(_id=None, comment_id=None):
# 	comment = Comment.objects(id=comment_id).first()
# 	strat = Strategy.objects(id=_id).first()
# 	return render_template("comments/edit.html", Strat=strat, comment=comment)

# @second.route("/<comment_id>", methods=["POST"])
# def comment_update(_id=None, comment_id=None):
# 	Comment.objects(id=comment_id).update(content=request.form["content"])
# 	for strat in Strats:
# 		strat.reload()
# 	return redirect("/strategies/" + _id)

@third.route('/<price_id>/delete', methods=["POST"])
def price_delete(_id=None, price_id=None):
	Price.objects(id=price_id).delete()
	return redirect("/strategies/" + _id)