from flask import Flask, render_template, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from os import environ
import json

app = Flask(__name__)
app.config['MONGO_URI'] = environ.get(
    'MONGODB_URI') or 'mongodb://localhost:27017/heroku-notepad'

mongo = PyMongo(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
#     'DATABASE_URL') or "sqlite:///notepad.sqlite"
# db = SQLAlchemy(app)


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    # tasks = db.session.query(Task)
    tasks = mongo.db.tasks.find({})
    data = []

    for task in tasks:
        item = {
            # "id": task.id,
            "_id": str(task['_id']),
            "description": task['description']
        }
        data.append(item)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
