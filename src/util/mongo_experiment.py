import os
from flask import Flask
from flask_pymongo import PyMongo
import pprint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'my_mongo_experiments'
app.config['MONGO_URI'] = 'mongodb://' + os.environ.get('DB_USER') + ':' + os.environ.get(
    'DB_PASS') + '@ds127536.mlab.com:27536/my_mongo_experiments'

mongo = PyMongo(app)


@app.route('/')
def first_page():
    return 'Welcome!'


@app.route('/find')
def find():
    """Finds the document with matching name."""
    about_me = mongo.db.about_me
    rana_details = about_me.find_one({'Name': 'Rana'})
    print("Here: ", rana_details)

    about_me_list = about_me.find({})
    for doc in about_me_list:
        print(doc)

    ret = 'Rana\'s Designation: ' + rana_details['Designation'] + ', Rana\'s Age: ' + str(rana_details['Age'])
    return ret


@app.route('/upsert')
def upsert():
    """If the Name is found update the Age,
    else insert a new document.
    """
    about_me = mongo.db.about_me
    about_me.update({'Name': 'Rana'}, {"$set": {'Age': 25}})
    rana_details = about_me.find_one({'Name': 'Rana'})
    print("Here: ", rana_details)
    return str(rana_details['Age'])


@app.route('/remove')
def remove():
    """Remove the document where the key is "AGE"""
    pass


if __name__ == '__main__':
    app.run(debug=True)
