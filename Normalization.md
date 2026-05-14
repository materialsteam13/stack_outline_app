*** Original Functional Dependencies ***
User Table:
    userID --> {userName, email, joinDate, lastLogin, totalTasksCompleted}
Calendar Table:
    calID --> {userID, deadlineDate, calName, cUpdatedAt}
Task Table:
    taskID --> {calID, taskName, taskDetails, isComplete, estPomos, actualPomos, rowVersion}

*** Anomoly Identification ***
Update:
    Since totalTasksCompleted is calculated from the task table, if the task table is updated and the update isn't forwarded to the user table, the count becomes off.
Insert:
    If a new task is added and the calendar ID isn't included, then the task won't show up on the calendar.
Delete:
    If a task is removed and the calendar isn't updated then it might still show up.