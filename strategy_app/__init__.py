from flask import Flask, render_template, request, redirect, url_for
import random 
from .extensions import *
from flask_bootstrap import Bootstrap
from .strategies import main
from .comments import second



app = Flask(__name__)
app.config.from_object("strategy_app.settings")
mongo.init_app(app)
Bootstrap(app)

app.register_blueprint(main)
app.register_blueprint(second, url_prefix="/strategies/<_id>/comments")
  

if __name__ == '__main__':
   app.run(debug=True)