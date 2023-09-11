from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("persons.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER
               )
               """)
db.commit()
@app.route("/persons", methods=["POST"])
def create_person():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    if name is None or age is None:
        return jsonify({"error": "Both 'name' and 'age' are required" }), 400
    cursor.execute("insert into persons (name, age) values (?, ?)", (name, age))
    db.commit()
    return jsonify({"message": "Person created successfully"}), 201

@app.route("/persons/<string:name>", methods=["GET", "PUT", "DELETE"])
def handle_person(name):
    if request.method == "GET":
        cursor.execute("select * from persons where name=?", (name,))
        person = cursor.fetchone()
        if person is None:
            return jsonify({"error" : "Person not found"}), 404
        return jsonify({"name": person[1], "age": person[2]})
    if request.method == "PUT":
        data = request.get_json()
        age = data.get("age")
        if age is None:
            return jsonify({"error": "Age is required for updating"}), 400
        cursor.execute("update persons set age=? where name=?", (age, name))
        db.commit()
        return jsonify({"message": "Person update successfully"})
    if request.method == "DELETE":
        cursor.execute("delete from persons where name=?", (name,))
        db.commit()
        return jsonify({"message": "Person deleted successfully"})
    if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)