# ORGANIZE-EM', THE MINIMALIST'S TASK MANAGER
#### Video Demo: <https://www.youtube.com/watch?v=9fcMObOzPD4>
#### Description:

Brief Project Description:
Organize-Em' is a minimalistic task managing website designed with simplicity and an intuitive design.
This website was developed using Python, Flask, HTML, CSS and SQL.
Organize-Em' contains a description of it's purpose along with brief instructions on how one can operate the website.

Using Organize-Em', one can create and remove tasks, whilst also being able to assign a priority level to a specific task (high, medium, low).
Tasks are displayed using a table created with HTML, with table data being stored in a SQL database.

The purpose of files:

Statics:

styles.css:
This css file contains presets created to simplify the creation of an aesthetic website. Text styles were created along with classes that
center align items.

Templates:

apology.html:
This template was adapted from CS50 problem set 9 "Finance". This template simply is called when an error is encountered and displays
an image along with an error code and description.

index.html:
This single template is the user interface for Organize-Em'. A single template was used to simplify the user experience, as having to access multiple
templates to simply create or remove a task is tedious.
Titles, paragraphs and images were created and styled using css classes.

A form was created to allow the user to input a "task" of type text whilst also being able to select a "priority" level from
a drop down menu created with the 'select' tag.
values were prefixes using numbers so that priorities can be organized numerically.

A "submit" button was used to send data to the back-end using a "submit" button.

A second form was created to allow users to remove a task. This form accepts an integer (task number) from the user and sends
the integer to the back-end where the task with an associated "task-id" will be removed.

A third form was created to allow users to organize tasks based on a cooresponding priority level. Tasks can be organized
from "high to low" or "low to high". These options can be selected from a drop down menu. These options have values of 0 and 1 respectively and
are sent to the back-end using a "submit" button.

A table was created that displays tasks, task #'s and task priorities. A for loop was used to iterate over items in a list found on the
server side. These items were displayed upon each iteration.

layout.html:
This html file was created to house jquery, bootstrap and misc headers whilst also linking the styles.css file. This file is inherited from by
every html template.

application.py:
This python file houses the logic that gives Organize-Em' functionallity.
Flask and SQL are imported such that additional functions can be used.
This python file consists of various functions such as "apology", "get_order" and "index".

functions:

The apology function was adapted from CS50 problem set 9 "Finance" and accepts a message as an input. This function renders the apology.html template
when called whilst passing the input message to the front-end.

The get_order function obtains the value from the "order" input present within index.html when called. This only occurs if the "order" input tag has
a value. This value is then stored in a variable and returned to the application.

The index function houses the majority of the functional logic.

Error handling:
An if statement is first defined checking for the request method "POST".
If the request method is "POST", a series of if statements then handle errors. Errors that will be handled include...
If no task is found, if no delete request is found and if a priority is not selected. These if statements call the apology function.
As some input forms cannot be distinguished the error message "No task/order found" is displayed on apology.html.

Adding a task:
The index function then checks to see if the "task" input tag has a value using an if statement. If a value is found,
variables "task" and "priority" hold the values found in the "task" input tag and the "priority" select tag.
These values are then stored in the SQL database.

Deleting a task:
An if statement checks to see if the "deltask" input tag has a value. If this is true, another nested if statement checks to see if the
input value is not a digit. If this is true, the apology function is called and the user is taken to apology.html.
If this is false, the variable "deltask" is assigned to the value of the "deltask" input tag. A SQL query then removes the task, with the id
that cooresponds to that of the users input.

Organizing by priority:
The "get_order" function is called and stored in the "order" variable. If statements checks for the value of the "order"
variable. If "order" is 1, a SQL query selects tasks, ids and priorities and orders then by decending priority. If "order is 0",
tasks, ids and priorities are ordered by accending priority. If no value for order is found, tasks, ids and priorities are organized in a que.
The variable "row" is assigned to each SQL query within each if statement which stores the value of the tasks, ids and priorities.

Populate table:
A list is initiated and called "tasklist". This list will hold all tasks, id's and priorities
respectively.
A for loop then iterates over each index in "rows" and assigns each id, task and priority to variables "caller", "item" and "level"
respectively. The values of these variables are then stored in a dictionary and appended to the end of "tasklist".

Render website:
The actual index.html template is then rendered using the "render_template" function passing arguments of
index.hrml and tasklist.

tasks.db: This SQL database contains the "users" table which has columns "id", "task" and "priority".
This is where the properties of a task will be contained and manipulated.
