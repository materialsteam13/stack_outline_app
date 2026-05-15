from .extensions import db

class User(db.Model):
    __tablename__ = 'User'
    userID = db.Column(db.String(8), primary_key=True)
    userName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    joinDate = db.Column(db.Date, nullable=False)
    lastLogin = db.Column(db.DateTime)

    # Requirement: One to Many relationship between User and Calendar (One User can have many Calendars, but each Calendar belongs to one User)
    # Allow user.calendars to access all related calendar objects
    calendars = db.relationship('Calendar', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.userName}>"
    
class Calendar(db.Model):
    __tablename__ = 'Calendar'
    calID = db.Column(db.String(15), primary_key=True)
    userID = db.Column(db.String(8), db.ForeignKey('User.userID'), nullable=False)
    calName = db.Column(db.String(50), nullable=False)
    deadlineDate = db.Column(db.DateTime, nullable=False)
    cUpdatedAt = db.Column(db.DateTime)

    # Requirement: One to Many relationship between Calendar and Task (One Calendar can have many Tasks, but each Task belongs to one Calendar)
    # Allows calendar.tasks to access all related task objects
    tasks = db.relationship('Task', backref='calendar', lazy=True)

    def __repr__(self):
        return f"<Calendar {self.calName}>"

class Task(db.Model):
    __tablename__ = 'Task'
    taskID = db.Column(db.Integer, primary_key=True)
    calID = db.Column(db.String(15), db.ForeignKey('Calendar.calID'), nullable=False)
    taskName = db.Column(db.String(50), nullable=False)
    taskDetails = db.Column(db.String(150))
    isComplete = db.Column(db.Boolean, default=False)
    estPomos = db.Column(db.Integer)
    actualPomos = db.Column(db.Integer)
    rowVersion = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f"<Task {self.taskName}>"