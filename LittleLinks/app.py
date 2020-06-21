import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env
  

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

@app.route('/')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/liveLearn')
def liveLearn():
    return render_template("liveLearn.html")

@app.route('/learningLinks')
def getLearn():
    return render_template("learningLinks.html", 
                          Little_Links=mongo.db.Little_Links.find())

@app.route('/learnCategories')
def add_links():
    return render_template('LittleLinks.html',
                           Category=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)




@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks =  mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.categories.find()
    category_list = [category for category in all_categories]
    return render_template('edit_task.html', task=the_task, categories=category_list)
@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.tasks
    tasks.update( {'_id': ObjectId(task_id)},
    {
        'task_name':request.form.get('task_name'),
        'task_vid':request.form.get('task_vid'),
        'category_name':request.form.get('category_name'),
        'task_description': request.form.get('task_description')
        # 'due_date': request.form.get('due_date'),
        # 'is_urgent':request.form.get('is_urgent')
    
    })
    return redirect(url_for('get_tasks'))
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('get_tasks'))
            

