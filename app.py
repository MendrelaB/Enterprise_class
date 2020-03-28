from flask import Flask, jsonify, request

app = Flask(__name__)

#@@ -19,5 +19,21 @@ 
#students = [
def hello():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_students():
    student = request.get_json()
    movies.append(student)
    return {'id': len(students)}, 200

@app.route('/students/<int:index>', methods=['PUT'])
def update_students(index):
    student = request.get_json()
    students[index] = student
    return jsonify(students[index]), 200

@app.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return 'None', 200

app.run()