from flask import Flask, render_template, request, redirect, url_for
import random 
from extensions import *
from flask_bootstrap import Bootstrap
from strategies import main
from comments import second
from prices import third
from six.moves import urllib



app = Flask(__name__)
# app.config.from_object("settings")
username = urllib.parse.quote_plus('enzols')
password = urllib.parse.quote_plus('ozneNon@m96')
client = "mongodb+srv://%s:%s@cluster0.fnjla.mongodb.net/python_project?retryWrites=true&w=majority" % (username, password)
app.config["MONGO_URI"] = client
mongo.init_app(app)
Bootstrap(app)

app.register_blueprint(main)
app.register_blueprint(second, url_prefix="/strategies/<_id>/comments")
app.register_blueprint(third, url_prefix="/strategies/<_id>/prices")  

if __name__ == '__main__':
   app.run(debug=True)