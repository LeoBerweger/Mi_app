from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
try:
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client['todo_app']  # Database name
    todos_collection = db['todos']  # Collection name
    # Quick test to verify connection
    client.admin.command('ping')
    print("Connected to MongoDB Atlas successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {e}")
    todos_collection = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    todos = []
    if todos_collection is not None:  # Changed from 'if todos_collection:'
        try:
            todos = list(todos_collection.find())
            print(f"Found {len(todos)} todos")
        except Exception as e:
            print(f"Error retrieving todos: {e}")
    return render_template('start.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    name = request.form.get('name')
    if name and todos_collection is not None:  # Changed from 'if name and todos_collection:'
        try:
            result = todos_collection.insert_one({'name': name})
            print(f"Added todo with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error adding todo: {e}")
    return redirect(url_for('start'))

if __name__ == '__main__':
    app.run(debug=True)