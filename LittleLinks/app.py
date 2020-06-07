import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
  import env as config
  

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')
@app.route('/live-learn')
def landing():
    return render_template("liveLearn.html")                           
@app.route('/landing')
def landing():
    return render_template("landing.html", 
                           LearningLinks=mongo.db.learnLink.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)



            

