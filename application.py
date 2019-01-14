from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

#from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
#if app.config["DEBUG"]:
 #   @app.after_request
  #  def after_request(response):
   #     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    #    response.headers["Expires"] = 0
     #   response.headers["Pragma"] = "no-cache"
      #  return response

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.route("/")
#@login_required
def index():
    # Run index
    return render_template("index.html")
