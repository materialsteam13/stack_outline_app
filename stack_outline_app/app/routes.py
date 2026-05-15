from flask import Blueprint, render_template

from .models import User, Calendar, Task

main = Blueprint("main", __name__)


#@main.route("/")
#def index():
    #records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
    #return render_template("index.html", records=records)

@main.route('/')
def index():
    # Fetch all tasks from the database
    all_tasks = Task.query.all() 

    import os
    print(f"DEBUG: Current Database Path: {os.getcwd()}")
    print(f"DEBUG: Found {len(all_tasks)} tasks in the database.")
    
    # Pass the tasks to the index.html template
    return render_template('index.html', tasks=all_tasks)
