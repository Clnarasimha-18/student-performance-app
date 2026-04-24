from flask import Flask, render_template, request
import json
from model import predict_student

app = Flask(__name__)

with open("students.json") as f:
    students = json.load(f)

# ✅ ADD HERE
@app.route('/students')
def student_list():
    return render_template('students.html', students=students)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    roll = request.form['roll']

    student = next((s for s in students if str(s["RollNo"]) == roll), None)

    if not student:
        return "Student not found!"

    result, status, study, cgpa = predict_student(student)

    return render_template(
        'result.html',
        student=student,
        result=result,
        status=status,
        study=study,
        cgpa=cgpa
    )

if __name__ == '__main__':
 app.run(debug=True, use_reloader=False)