# Project Description
Project Katch-Up is my Senior Design project. This database is created as a piece of what our database
on that project might look like. This project tackles User, Calendar, and Task tables and their relations.
It tracks tasks in a list on a calendar related to a user. The tasks keep a track of the Pomodoros it took
to complete the assignment.

# Stack Outline App

Barebones project outline for:
- Python 3
- Flask backend
- Relational DB (SQLite by default)
- SQLAlchemy ORM
- HTML5/CSS3 frontend with Bootstrap and Jinja2 templates
- Git version control

## Project Structure

```
stack_outline_app/
  app/
    __init__.py
    extensions.py
    models.py
    routes.py
    static/css/styles.css
    templates/base.html
    templates/index.html
  config.py
  run.py
  requirements.txt
  .env.example
  .gitignore
  NORMALIZATION.md
  AI_LOG.md
```

## Quick Start

1. Create and activate a virtual environment.
   ```
   python -m venv venv   
   venv\Scripts\activate 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open http://127.0.0.1:5000

## Notes

- SQLite is used out of the box via `DATABASE_URL=sqlite:///katchup.db`.
- To switch databases, set `DATABASE_URL` (for example, PostgreSQL/MySQL URI) and install the corresponding driver.
- Tables are auto-created at startup for this minimal starter (`db.create_all()`).
- ZyBooks Web Programming book was used to reference HTML and CSS. This was obtained through Prof. Bagai's Web Programming class this semester.
- Python.org was consulted for syntax review.

# Usage
To run the application:
   flask run

Open your browser to:
   http://127.0.0.1:5000

Features
- Dashboard: view total tasks and pomodoros logged using the SQL aggregate functions
- Create: add new tasks to the list
- Update: log pomodoros or mark tasks as complete
- Delete: remove tasks from the database.
