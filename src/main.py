import sqlite3
from flask import *
import json
from person import Person

app = Flask(__name__)


def go_home():
    c = sqlite3.connect("task.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Tasks(id TEXT, name TEXT, task TEXT, status TEXT)")
    c.connection.close()


@app.route('/', methods=['GET'])
def home():
    go_home()
    return 'Welcome to the To Do API!'


@app.route('/getTasks', methods=['GET'])
def get_students():
    c = sqlite3.connect("task.db").cursor()
    c.execute("SELECT * FROM TASKS")
    data = c.fetchall()
    return jsonify(data)


@app.route('/getTaskById/<student_id>', methods=['GET'])
def get_task_by_id(task_id):
    c = sqlite3.connect("task.db").cursor()
    c.execute("SELECT * FROM TASKS WHERE id=?", (task_id,))
    data = c.fetchone()
    return json.dumps(data)


@app.route('/addTask', methods=['POST', 'GET'])
def add_student():
    db = sqlite3.connect("task.db")
    c = db.cursor()
    person = Person(request.form["name"], request.form["task"], request.form["status"])
    print(person)
    c.execute("INSERT INTO TASKS VALUES(?,?,?,?)", (person.id, person.name, person.task, person.status))
    db.commit()
    data = c.lastrowid
    return json.dumps(data)


@app.route('/updateTask/<task_id>', methods=['PUT'])
def update_task(task_id):
    db = sqlite3.connect("task.db")
    c = db.cursor()
    person = Person(request.form["name"], request.form["task"], request.form["status"])
    print(person)
    c.execute("UPDATE TASKS SET name = ?, task =?, status =? WHERE id=?",
              (person.name, person.task, person.status, task_id))
    db.commit()
    return json.dumps("Record was successfully updated")


@app.route('/deleteTask/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = sqlite3.connect("task.db")
    c = db.cursor()
    c.execute("DELETE FROM TASKS WHERE id=?", (task_id,))
    db.commit()
    return json.dumps("Record was successfully deleted")


# driver function
if __name__ == '__main__':
    app.run(debug=True)
