import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone3_edm'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone3_edm?retryWrites=true'

mongo = PyMongo(app)

@app.route('/get_festivals')
def get_festivals():
    return render_template("festivals.html", festivals=mongo.db.festivals.find())
    
@app.route('/add_festival')
def add_festival():
    return render_template('addfestival.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        