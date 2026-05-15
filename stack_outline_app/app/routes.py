from flask import Blueprint, render_template, request, redirect, url_for
from .models import User, Calendar, Task
from .extensions import db
from sqlalchemy import func

main = Blueprint("main", __name__)


#@main.route("/")
#def index():
    #records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
    #return render_template("index.html", records=records)

@main.route('/')
def index():
    # Fetch all tasks from the database
    all_tasks = Task.query.all() 

    #Aggregate Functions
    total_tasks = db.session.query(func.count(Task.taskID)).scalar() or 0
    completed_tasks = db.session.query(func.count(Task.taskID)).filter(Task.isComplete == True).scalar() or 0
    total_pomos = db.session.query(func.sum(Task.actualPomos)).scalar() or 0

    # Pass the tasks to the index.html template
    return render_template('index.html', tasks=all_tasks, total_tasks=total_tasks, completed_tasks=completed_tasks, total_pomos=total_pomos )

@main.route('/add', methods=['POST'])
def add_task():
    name = request.form.get('name', '').strip()
    est_str = request.form.get('est_pomos', '1')

    # Server-Side Validation (Requirement 30)
    if not name:
        # Prevents empty task names
        return "Task name cannot be empty", 400
    
    try:
        est = int(est_str)
        if est < 1:
            # Prevents negative or zero pomodoro estimates
            return "Estimate must be at least 1", 400
    except ValueError:
        return "Invalid number for estimate", 400

    new_task = Task(
        taskName=name, 
        estPomos=est, 
        calID='CAL001', 
        isComplete=False, 
        actualPomos=0
    )

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    # Fetch the specific task by its ID
    task = Task.query.get_or_404(task_id)
    
    # Update the status
    task.isComplete = True
    
    # Commit the change
    db.session.commit()
    
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Find the task
    task = Task.query.get_or_404(task_id)
    
    # Remove it from the session
    db.session.delete(task)
    
    # Commit the change to the .db file
    db.session.commit()
    
    return redirect(url_for('main.index'))