# app.py
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
import datetime # Keep for potential future use with timestamps

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.static_folder = 'static' # Explicitly set static folder

# MongoDB Atlas connection
try:
    mongo_uri = os.getenv("MONGO_URI")
    # AddretryWrites=false to connection string if facing issues with older servers
    client = MongoClient(mongo_uri)
    db = client['todo_app']  # Database name
    todos_collection = db['todos']  # Collection name
    # Quick test to verify connection
    client.admin.command('ping')
    print("Connected to MongoDB Atlas successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {e}")
    # In a real app, you might want to handle this more gracefully
    # perhaps by showing an error page or disabling DB features.
    todos_collection = None

@app.route('/')
def index():
    # Redirect root to the start page with the default filter
    return redirect(url_for('start', filter='active'))

@app.route('/start')
def start():
    current_filter = request.args.get('filter', 'active') # Default to 'active'
    todos = []
    mongo_query = {} # Default query (empty means 'all')

    if current_filter == 'active':
        mongo_query = {'completed': False}
    elif current_filter == 'completed':
        mongo_query = {'completed': True}
    # No specific query needed for 'all' - {} finds all documents

    if todos_collection is not None:
        try:
            # Apply the filter query
            # You could add sorting here, e.g., by name:
            # todos = list(todos_collection.find(mongo_query).sort('name', 1))
            todos = list(todos_collection.find(mongo_query))
            print(f"Found {len(todos)} todos matching filter '{current_filter}'")
        except Exception as e:
            print(f"Error retrieving todos: {e}")
            # Consider flashing an error message to the user
            # from flask import flash
            # flash(f"Error retrieving tasks: {e}", "danger")

    return render_template(
        'start.html',
        todos=todos,
        current_filter=current_filter # Pass filter to template
    )

@app.route('/add_todo', methods=['POST'])
def add_todo():
    name = request.form.get('name')
    if name and todos_collection is not None:
        try:
            # Add new todos with completed set to False
            # Add created_at and updated_at here when ready
            new_todo = {
                'name': name,
                'completed': False,
                # 'created_at': datetime.datetime.utcnow(),
                # 'updated_at': datetime.datetime.utcnow()
            }
            result = todos_collection.insert_one(new_todo)
            print(f"Added todo with ID: {result.inserted_id}")
            # Optionally flash a success message
            # flash(f"Task '{name}' added successfully!", "success")
        except Exception as e:
            print(f"Error adding todo: {e}")
            # flash(f"Error adding task: {e}", "danger")

    # Redirect back to the default 'active' view after adding
    return redirect(url_for('start', filter='active'))

@app.route('/complete/<task_id>', methods=['POST'])
def complete_todo(task_id):
    redirect_filter = request.args.get('current_filter', 'active') # Get filter from URL param if passed

    if todos_collection is not None:
        try:
            oid = ObjectId(task_id)
            # Find the current task to toggle its status
            task = todos_collection.find_one({'_id': oid})
            if task:
                new_status = not task.get('completed', False)
                update_data = {
                    '$set': {
                        'completed': new_status,
                        # 'updated_at': datetime.datetime.utcnow() # Update timestamp
                    }
                }
                result = todos_collection.update_one({'_id': oid}, update_data)
                print(f"Updated task {task_id} completed status to {new_status}. Matched: {result.matched_count}")
            else:
                 print(f"Task with ID {task_id} not found for completion.")
                 # flash(f"Task not found.", "warning")
        except Exception as e:
            print(f"Error completing/toggling todo {task_id}: {e}")
            # flash(f"Error updating task: {e}", "danger")

    # Redirect back to the view the user was on
    return redirect(url_for('start', filter=redirect_filter))


@app.route('/delete/<task_id>', methods=['POST'])
def delete_todo(task_id):
    redirect_filter = request.args.get('current_filter', 'active') # Get filter from URL param if passed

    if todos_collection is not None:
        try:
            oid = ObjectId(task_id)
            result = todos_collection.delete_one({'_id': oid})
            if result.deleted_count == 1:
                print(f"Deleted task with ID: {task_id}")
                # flash("Task deleted.", "success")
            else:
                print(f"Task with ID {task_id} not found for deletion.")
                # flash("Task not found for deletion.", "warning")
        except Exception as e:
            print(f"Error deleting todo {task_id}: {e}")
            # flash(f"Error deleting task: {e}", "danger")

    # Redirect back to the view the user was on
    return redirect(url_for('start', filter=redirect_filter))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)