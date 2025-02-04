from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

with open('data.json') as f:
  data = json.load(f)


@app.route('/')
def hello_world():
  return 'Hello, World!'  

@app.route('/students')
def get_students() :
  result = []
  pref = request.args.get('pref') 
  if pref:
    for student in data: 
      if student['pref'] == pref: 
        result.append(student) 
    return jsonify(result) 
  return jsonify(data) 


@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return jsonify(student)
  return f"Student {id} does not exist"

@app.route('/stats')
def get_stats():
  allStats = {
    "Computer Science (Major)": 0,
    "Computer Science (Special)": 0,
    "Information Technology (Major)": 0,
    "Information Technology (Special)": 0,
    "Vegetable": 0,
    "Chicken": 0,
    "Fish": 0
  }
  
  for student in data:
    pref = student.get('pref')
    programme = student.get('programme')
    if pref in allStats:
      allStats[pref] += 1
    if programme in allStats:
      allStats[programme] += 1
  print(allStats)
  return jsonify(allStats)

@app.route('/add/<a>/<b>')
def add(a, b):
  a = int(a)
  b = int(b)
  res = a + b
  return jsonify(res)

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
  a = int(a)
  b = int(b)
  res = a - b
  return jsonify(res)

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
  a = int(a)
  b = int(b)
  res = a * b
  return jsonify(res)

@app.route('/divide/<a>/<b>')
def divide(a, b):
  a = int(a)
  b = int(b)
  if b == 0:
    error_message = {
      "error": "Invalid Division",
      "message": "Cannot divide by zero."
    }
    return jsonify(error_message)
  res = a / b
  return jsonify(res)

app.run(host='0.0.0.0', port=8080, debug=True)
