from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Calendar, Task
from .extensions import db

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

@main.route('/add', methods=['POST'])
def add_task():
    # 1. Get data from the form
    name = request.form.get('name')
    est = request.form.get('est_pomos')

    # 2. Create a new Task object (assuming userID 1 for now)
    new_task = Task(taskName=name, estPomos=est, calID='CAL001', isComplete=False, actualPomos=0)

    # 3. Save to database
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    # 1. Fetch the specific task by its ID
    task = Task.query.get_or_404(task_id)
    
    # 2. Update the status
    task.isComplete = True
    
    # 3. Commit the change
    db.session.commit()
    
    return redirect(url_for('main.index'))