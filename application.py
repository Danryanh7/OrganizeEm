import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tasks.db")

# apology function Adapted from CS50 problem set 9 "finance"
def apology(message, code= 400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def get_order():
    if request.form.get("order"):
        order = request.form.get("order")
        return order

#Generates the home page
@app.route("/", methods=["GET", "POST"])
def index():
    #Make rows a global variable so it can be assigned when a priority order is chosen
    rows=None

    #Checks for request method "Post"
    if request.method == "POST":
        #HANDLE ERRORS
        #If no task or delete request is found, throw error
        if not request.form.get("task") and not request.form.get("deltask") and not request.form.get("order"):
            return apology("No Task / Order Found")

        #If no priority is found, and a task is selected, throw error
        if request.form.get("task") and not request.form.get("priority"):
            return apology("Please select a priority")

        #Add task
        if request.form.get("task"):
            task = request.form.get("task")
            priority = request.form.get("priority")

            db.execute("INSERT INTO users (task, priority) VALUES (:task,:priority)", task=task, priority=priority)
            return redirect("/")

        #Delete task
        if request.form.get("deltask"):
            #Checks to see if ID is a number
            if not request.form.get("deltask").isdigit():
                return apology("Invalid task ID")
            else:
                deltask = request.form.get("deltask")
                db.execute("DELETE FROM users WHERE id = ?", deltask)
                return redirect("/")

    #End of if loop, carry on data
    #Order by priority
    order = get_order()

    if order == "1":
        rows = db.execute("SELECT task,id,priority FROM users ORDER BY PRIORITY DESC")
    elif order == "0":
        rows = db.execute("SELECT task,id,priority FROM users ORDER BY PRIORITY")
    else:
        rows = db.execute("SELECT task,id,priority FROM users")

    #Populates tasklist
    tasklist = []

    for row in rows:
        caller = row["id"]
        item = row["task"]
        level = row["priority"]
        #Priority excludes organizer
        tasklist.append({"task":item, "id":caller, "priority":level[1:]})

    #Returns actual website
    return render_template("index.html", tasklist=tasklist)