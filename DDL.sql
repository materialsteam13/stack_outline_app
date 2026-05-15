-- Enable Foreign Key Support for SQLite
PRAGMA foreign_keys = ON;

-- DDL Table 
DROP TABLE IF EXISTS Task;
DROP TABLE IF EXISTS Calendar;
DROP TABLE IF EXISTS User;

-- Create the User Table
CREATE TABLE User (
    userID VARCHAR(8) NOT NULL,
    userName VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    joinDate DATE NOT NULL,
    lastLogin DATETIME,
    PRIMARY KEY (userID)
);

-- Create the Calendar Table
CREATE TABLE Calendar (
    calID VARCHAR(15) NOT NULL,
    userID VARCHAR(8) NOT NULL,
    deadlineDate DATETIME NOT NULL,
    calName VARCHAR(50) NOT NULL,
    cUpdatedAt DATETIME,
    PRIMARY KEY (calID),
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
);

-- Create the Task Table
CREATE TABLE Task (
    taskID INTEGER PRIMARY KEY AUTOINCREMENT,
    calID VARCHAR(15) NOT NULL,
    taskName VARCHAR(50) NOT NULL,
    taskDetails VARCHAR(150),
    isComplete INTEGER DEFAULT 0,
    estPomos INT,
    actualPomos INT,
    rowVersion INT NOT NULL DEFAULT 1,
    FOREIGN KEY (calID) REFERENCES Calendar(calID) ON DELETE CASCADE
);

SELECT 'DDL PHASE COMPLETE' AS STATUS;