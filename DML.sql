SELECT 'DML START' AS Status;
-- Part 3: DML: Table Entries and Table Updates
-- User Table Entries
INSERT INTO User (userID, userName, email, joinDate, lastLogin) VALUES
('U859H824', 'Ashdon Kice', 'ajkice@shockers.wichita.edu', '2024-08-11', '2026-04-12 12:00:00'),
('A123B456', 'Luke Skywalker', 'lastjedi@gmail.com', '2020-11-06', '2026-04-12 12:45:00'),
('C123D456', 'Boba Fett', 'bounty@hunters.edu', '2021-03-10', '2026-04-12 12:20:00'),
('E123F456', 'Echo FiveOFirst', 'cloneTrooper1409@republic.com', '2022-01-21', '2026-04-12 12:08:00'),
('G123H456', 'Obi-Wan Kenobi', 'imissquigan@jedi.republic.com', '2023-05-01', '2026-04-12 12:12:00');

-- Calendar Table Entries
INSERT INTO Calendar (calID, userID, deadlineDate, calName, cUpdatedAt) VALUES
('CAL-001', 'U859H824', '2026-05-10 23:59:59', 'Spring Finals', '2026-04-08 09:00:01'),
('CAL-002', 'A123B456', '2026-05-15 23:59:59', 'Senior Project', '2026-01-04 14:52:21'),
('CAL-003', 'C123D456', '2026-04-29 23:59:59', 'WSU Assignments', '2026-02-17 12:40:40'),
('CAL-004', 'E123F456', '2026-05-01 23:59:59', 'Homework', '2026-03-12 08:04:12'),
('CAL-005', 'G123H456', '2026-04-17 23:59:59', 'Dooms Day', '2026-01-01 01:01:01');

-- Task Table Entries
INSERT INTO Task ( calID, taskName, taskDetails, isComplete, estPomos, actualPomos, rowVersion) VALUES
('CAL-001', 'Web Programming Ch. 5', 'CSS Fundamentals', 0, 4, 0, 1),
('CAL-001', 'Web Programming Ch. 6', 'Java Script', 1, 2, 3, 2),
('CAL-002', 'Databases Project 2', '4 parts, 1 part a day', 0, 8, 0, 2),
('CAL-003', 'Bounty Hunters Update List', 'Search for the latest bounties', 1, 1, 2, 1),
('CAL-004', 'Calculus Homework', 'Calc 7.3', 0, 6, 7, 1);

-- 1. Update a Date 
UPDATE Calendar SET deadlineDate = '2026-05-04 12:00:00' WHERE calID = 'CAL-005';

-- 2. Update Meta Data
UPDATE Task SET rowVersion = rowVersion + 1 WHERE taskName = 'Web Programming Ch. 5';

-- 3. Remove a record
DELETE FROM Task WHERE taskName = 'Calculus Homework';

SELECT 'DML PHASE COMPLETE' AS Status;