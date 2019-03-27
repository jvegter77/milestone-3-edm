import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone3_edm'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone3_edm?retryWrites=true'

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_festivals')
def get_festivals():
    return render_template("index.html", festivals=mongo.db.festivals.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        