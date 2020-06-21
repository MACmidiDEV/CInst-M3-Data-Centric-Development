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
@app.route('/landing') 
def landing():
    return render_template("home.html")  
@app.route('/getLearn')         
def getLearn():
    return render_template("learningLinks.html", Learning_Links=mongo.db.Learning_Links.find())   
@app.route('/add_link')
def add_link():
    return render_template('add_link.html',
                           Categories=mongo.db.Categories.find())        
@app.route('/insert_link', methods=['POST'])
def insert_link():
    LearningLinks = mongo.db.Learning_Links  
    LearningLinks.insert_one(request.form.to_dict())    
    return redirect(url_for('getLearn'))    
@app.route('/edit_link/<link_id>')
def edit_link(link_id):
    the_link = mongo.db.Learning_Links.find_one({"_id": ObjectId(link_id)})
    all_categories =  mongo.db.Categories.find()
    return render_template('edit_link.html', link=the_link, Categories=all_categories)
@app.route('/update_link/<link_id>', methods=["POST"])
def update_link(link_id):
    links = mongo.db.Learning_Links
    links.replace_one( {'_id': ObjectId(link_id)},
    {
        'learn_link':request.form.get('learn_link'),  
        'mentor_message':request.form.get('mentor_message'),
        'category_name':request.form.get('category_name')
    })
    return redirect(url_for('getLearn'))                         
@app.route('/delete_link/<link_id>')
def delete_link(link_id):
    mongo.db.Learning_Links.delete_many({"_id":ObjectId(link_id)})
    return redirect(url_for('getLearn')) 
@app.route('/liveLearn')
def liveLearn():
    return render_template("liveLearn.html")   
@app.route('/get_categories')    
def get_categories():
    return render_template('categories.html', Categories=mongo.db.Categories.find())
@app.route('/add_category')
def add_category():
    return render_template('add_category.html')   
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.Categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))    
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category =  mongo.db.Categories
    category.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))    
@app.route('/edit_category/<category_id>')    
def edit_category(category_id):
    return render_template('edit_category.html', category=mongo.db.Categories.find_one({'_id': ObjectId(category_id)}))
@app.route('/update_category/<category_id>', methods=['POST'])        
def update_category(category_id):
    Categories = mongo.db.Categories
    Categories.update( 
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')}
    )
    return redirect(url_for('get_categories'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=0)