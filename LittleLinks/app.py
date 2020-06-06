import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
  import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')

@app.route('/landing')
def landing():
    return render_template("landing.html")

@app.route('/get_linkLearning')
def get_linkLearning():
    return render_template("linkLearning.html", 
                           linkLearning=mongo.db.learnLink.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)



            

