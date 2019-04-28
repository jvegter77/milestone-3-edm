import os
from flask import Flask, flash, render_template, redirect, request, url_for, session, abort, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone3_edm'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-gdxlz.mongodb.net/milestone3_edm?retryWrites=true'
app.secret_key = 'G0-Èl@E'

mongo = PyMongo(app)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/get_festivals')
def get_festivals():
    return render_template('festivals.html', festivals=mongo.db.festivals.find().sort('_id',1))
    
@app.route('/add_festival')
def add_festival():
    return render_template('addfestival.html')
    
@app.route('/insert_festival', methods=['POST'])
def insert_festival():
    festivals = mongo.db.festivals
    festivals.insert_one(request.form.to_dict())
    return redirect(url_for('get_festivals'))

@app.route('/edit_festival/<festival_id>')
def edit_festival(festival_id):
    the_festival = mongo.db.festivals.find_one({'_id': ObjectId(festival_id)})
    return render_template('editfestival.html', festival=the_festival)
    
@app.route('/update_festival/<festival_id>', methods=['POST'])
def update_festival(festival_id):
    festivals = mongo.db.festivals
    festivals.update( {'_id': ObjectId(festival_id)},
    {
        'festivalname': request.form.get('festivalname'),
        'startdate': request.form.get('startdate'),
        'enddate': request.form.get('enddate'),
        'location': request.form.get('location'),
        'website': request.form.get('website'),
        'tickets': request.form.get('tickets'),
        'image': request.form.get('image'),
        'comment': request.form.get('comment')
    })
    return redirect(url_for('get_festivals'))
    
@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/get_member')
def get_member():
    return render_template('memberpage.html', members=mongo.db.members.find())
    
@app.route('/add_member', methods=['POST'])
def add_member():
    members = mongo.db.members
    members.insert_one(request.form.to_dict())
    return redirect(url_for('get_member'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        