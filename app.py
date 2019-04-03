import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone3_edm'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone3_edm?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/get_festivals')
def get_festivals():
    return render_template('festivals.html', festivals=mongo.db.festivals.find())
    
@app.route('/add_festival')
def add_festival():
    return render_template('addfestival.html')
    
@app.route('/insert_festival', methods=['POST'])
def insert_festival():
    festivals = mongo.db.festivals
    festivals.insert_one(request.form.to_dict())
    return redirect(url_for('get_festivals'))

@app.route('/edit_festival/<festivals_id>')
def edit_festival(festivals_id):
    festivals = mongo.db.festivals.find_one({'_id': ObjectId(festivals_id)})
    all_festivals = mongo.db.festivals.find()
    return render_template('editfestival.html')
      

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        