from flask import Flask, render_template, request, redirect, url_for
import random 
from extensions import *
from flask_bootstrap import Bootstrap
from strategies import main
from comments import second
from prices import third



app = Flask(__name__)
# app.config.from_object("settings")
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo.init_app(app)
Bootstrap(app)

app.register_blueprint(main)
app.register_blueprint(second, url_prefix="/strategies/<_id>/comments")
app.register_blueprint(third, url_prefix="/strategies/<_id>/prices")  

if __name__ == '__main__':
   app.run(debug=True)