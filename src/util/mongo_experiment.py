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
    about_me.update({'Name': 'Rana'}, {"$set": {'Age': 22}}, upsert=True)
    rana_details = about_me.find_one({'Name': 'Rana'})
    print("Here: ", rana_details)
    return str(rana_details['Age'])


@app.route('/remove_doc')
def remove_doc():
    """Remove the document with matching name."""
    about_me = mongo.db.about_me
    to_remove = 'Ranas'
    about_me.remove({'Name': to_remove})
    return "Removed " + to_remove


@app.route('/remove')
def remove():
    """Remove the key "AGE" in any doc."""
    return "In Progress"


if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    app.run(host='0.0.0.0', port=port)
