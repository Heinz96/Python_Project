from flask import Blueprint, render_template, request, redirect, url_for
from extensions import *
from models.strategy import *
from pricing.Black_Scholes import *
from pricing.autocall import *
from pricing.Monte_Carlo import *

third = Blueprint("third", __name__)


#Inserting a price
@third.route("", methods=["POST"])
def price_post(_id=None):
    Option=request.form["Option"]
    S=float(request.form["S"])
    K=float(request.form["K"])
    r=float(request.form["r"])/100
    sigma=float(request.form["sigma"])/100
    t=float(request.form["t"])

    if Option!="Autocall":
        #Pricing type only if not autocall, there is no BS formula for Autocalls
        if request.form["Pricing"]=="BS":
            if Option=="Call":
                C = call(S, K, sigma, r, t)
            elif Option =="Put":
                C = put(S, K, sigma, r, t)
        elif request.form["Pricing"]=="MC":
            C = Monte_Carlo(10**6, S, K, r, sigma, t, Option)
        #Inserting in the database
        newPrice = Price(Option=Option,S=S,K=K,r=r,sigma=sigma,t=t,C=C).save()
    elif Option=="Autocall":
        #Inputting coupon and barrier, only in autocall
        Coupon=float(request.form["Coupon"])
        Barrier=float(request.form["Barrier"])
        C = autocall_pricing(np, 10**6, r, sigma, t, S, K, Coupon, Barrier)
        newPrice = Price(Option=Option,S=S,K=K,r=r,sigma=sigma,t=t,C=C,Coupon=Coupon,Barrier=Barrier).save()
    
    #Connecting the price to the correct strategy
    strat = Strategy.objects(id=_id).first()
    strat.prices.append(newPrice)
    strat.save()
    #Reloading the strategies
    for strat in Strats:
        strat.reload()
    return redirect("/strategies/" + _id)


#Deleting a price
@third.route('/<price_id>/delete', methods=["POST"])
def price_delete(_id=None, price_id=None):
	Price.objects(id=price_id).delete()
	return redirect("/strategies/" + _id)