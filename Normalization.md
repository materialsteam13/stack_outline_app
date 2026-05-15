*** Original Functional Dependencies / 1NF ***
User Table:
    Primary Key: userID --> {userName, email, joinDate, lastLogin, totalTasksCompleted}
Calendar Table:
    Primary Key: calID --> {userID, deadlineDate, calName, cUpdatedAt}
Task Table:
    Primary Key: taskID --> {calID, taskName, taskDetails, isComplete, estPomos, actualPomos, rowVersion}

*** Anomoly Identification ***
Update:
    Since totalTasksCompleted is calculated from the task table, if the task table is updated and the update isn't forwarded to the user table, the count becomes off.
Insert:
    If a new task is added and the calendar ID isn't included, then the task won't show up on the calendar.
Delete:
    If a task is removed and the calendar isn't updated then it might still show up.

*** 2NF Is complete since my primary keys are not composite ***

*** 3NF Break Down ***
Derived Data issue in User Table:
     `totalTasksCompleted` depended on the state of the Task table rather than the userID alone.
**Action:** Removed `totalTasksCompleted` from the User entity definition to prevent data                  desynchronization (Update Anomaly).
Result: Schema is in 3NF. All non-key attributes depend on "the key, the whole key, and nothing but the key."

*** Final 3NF Relations ***
1. User(userID [PK], userName, email, joinDate, lastLogin)
2. Calendar(calID [PK], userID [FK], calName, deadlineDate, cUpdatedAt)
3. Task(taskID [PK], calID [FK], taskName, taskDetails, isComplete, estPomos, actualPomos, rowVersion)