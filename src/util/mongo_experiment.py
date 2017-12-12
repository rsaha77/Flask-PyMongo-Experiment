import os
from flask import Flask
from flask_pymongo import PyMongo
import pprint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'my_mongo_experiments'
app.config['MONGO_URI'] = 'mongodb://' + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASS') + '@ds127536.mlab.com:27536/my_mongo_experiments'

mongo = PyMongo(app)


@app.route('/')
def first_page():
    return 'Welcome!'


@app.route('/find')
def find():
    
    about_me = mongo.db.about_me
    rana_details = about_me.find_one({'Name': 'Rana'})
    print("Here: ", rana_details)

    about_me_list = about_me.find({})
    for doc in about_me_list:
        print(doc)

    return 'Rana\'s Designation: ' + rana_details['Designation']


if __name__ == '__main__':
    app.run(debug=True)
