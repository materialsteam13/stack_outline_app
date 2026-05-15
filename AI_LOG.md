# AI Log Document
## AI Used: Gemini 3 Flash
## Other AI Input: Copilot predictive line suggestions were used as well.

# Prompts:
* Entry: 
Will my professor get an issue with the SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/ashar/Desktop/CodingSoftware/IntroDatabases/katchup.db' when he runs this code?
* AI Output:
A recommendation to abandon the hardcoded absolute Windows file path because it breaks portability across different machines. The AI suggested using Python's os library to calculate a relative path (sqlite:///' + os.path.join(basedir, '..', 'katchup.db')) based on the position of config.py.
* Verification
Verified the application's folder structure. Adjusted the os.path.join parameters to climb exactly one directory level out of the stack_outline_app directory to reliably target the root database file, katchup.db, without throwing errors on startup.

* Entry:
Pasted a Python stack trace ending with: TypeError: 'userID' is an invalid keyword argument for Task
* AI Output:
Identified a mismatch between the route's POST controller argument keys and the model's attributes. Explained that the generated SQLAlchemy __init__ constructor rejected the column name because it did not exist inside the target class schema.
* Verification:
Audited models.py. Discovered that the Task class does not maintain a direct relational foreign key for userID; instead, it maps to a Calendar via calID. Corrected the routes.py implementation to build the model object using calID='CAL001', preserving the schema's 3rd Normal Form relationship constraints.

* Entry:
I have this Database project due Thursday. Can you create me a timeline breaking down everything required for this project in its steps along with approximate time sink? 
* AI Output:
A 4 phase plan breaking down Project 3 into Database & Documention, Backend Foundation & CRUD, Frontend & Advanced Logic, and Polishing & AI Logging. Also generated a Quick Reference Table of mandatory deliverables. Listed: 5 git commits minimum, 3rd NF, SQL Schema, README.md, and AI_LOG.md.
* Verification:
Compared back to the CS665_Project3.pdf to see if there were any discrepancies. It had recommended using JavaScript because of it noting that I had done some recent projects in JavaScript (I took the Web Design class this semester and had Gemini chalk up a summer project to create a website in JavaScript for my resume).

* Entry:
Can I have you generate a Python3 cheatsheet of commands for me to review. I haven't coded in python in some time, emphasize commands examples of what you think could appear in this project?
* AI Output:
A list of 5 different section to review with Python code in mind. First being Flask & SQLAlchemy. Commands listed: Query All, Query by ID, Add & Commit, Delete, Filter. Each command came with a 1 sentence overview (i.e. tasks = Task.query.all() — Fetches every row in a table.). Second being SQL Aggregate Functions mentioning count, sum, and average. Section 3 contained Data Validation & Logic mentioning string cleaning, type casting, and checking relationships. Section 4 was over imports including: flask, sqlalchemy, and os. Section 5 was a review of Git commands: status, add ., commit, and push.
* Verification:
I checked the python commands along with some syntax with the documentation on www.python.org. Git commands were validated from Prof. Cody's lecture to Senior Design 1. 

* Entry:
What would you recommend for the AI_Log.md?
* AI Output:
"For your AI_LOG.md, we want to be completely transparent while showing your professor that you didn't just blindly copy and paste code. The rubric explicitly wants to see your modification and verification process." Then sectioned off 3 examples of "Entry: ... AI Output: ... and Verification: ...".
* Verification:
Checked Section 4 of the Project 3 pdf that said to mention the tool, prompt, output, and your modification. The 3 mentioned examples were formated into the first 3 entries listed in this document. I will add I was disappointed it didn't grab every entry, which is why the rest of these have been done by hand.

* Entry:
Our professor wanted us to use a virtual enviroment. I ran python -m venv .venv and have done a bit of work since then. But when I open the project now I get this:
PS C:\Users\ashar\Desktop\CodingSoftware\IntroDatabases> c:\Users\ashar\Desktop\CodingSoftware\IntroDatabases\.venv\Scripts\activate
c:\Users\ashar\Desktop\CodingSoftware\IntroDatabases\.venv\Scripts\activate : The term 
'c:\Users\ashar\Desktop\CodingSoftware\IntroDatabases\.venv\Scripts\activate' is not recognized as the name of a cmdlet, function, script file, or 
operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ c:\Users\ashar\Desktop\CodingSoftware\IntroDatabases\.venv\Scripts\ac ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (c:\Users\ashar\...cripts\activate:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
* AI Output
Mentioned that this is a classic Windows PowerShell Struggle. Walked through finding activate.ps1 and when I told it I didn't have one, it determined that the venv I ran the first time didn't complete. Gave me commands to remove the broken environment and recreate it.
* Verification:
Having the python -m venv .venv match with the Project 3 Setup Instructions I followed the rm -r .venv and did an watched the files update in VSCode file tree to see what files came back and the new files showed up.

* Entry:
Where on the github page should I find the link to submit to my professor?
* AI Output:
Copy the link in the address bar from wihtin the repository.
* Verification:
Realization that I was overcomplicating turning this assignment in looking for a "share link" like it was a google doc.