import json
import random

male_names = [
    "Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Krishna","Rahul","Rohan","Karthik"
]

female_names = [
    "Sneha","Ananya","Pooja","Kavya","Divya","Meena","Swathi","Aishwarya","Ritika","Neha"
]

last_names = [
    "Reddy","Sharma","Naidu","Rao","Kumar","Patel","Gupta","Verma","Yadav","Singh"
]

branches = ["CSE", "ECE", "EEE", "IT", "MECH", "CIVIL"]

courses_map = {
    "CSE": ["DSA", "DBMS", "OS", "AI"],
    "ECE": ["Signals", "VLSI", "Communication"],
    "EEE": ["Circuits", "Machines", "Power Systems"],
    "IT": ["Web Dev", "Cloud", "Cyber Security"],
    "MECH": ["Thermodynamics", "Design"],
    "CIVIL": ["Structures", "Surveying"]
}

students = []   # ✅ resets data every time

for i in range(100, 301):   # ✅ unique roll numbers

    # Decide gender first
    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first = random.choice(male_names)
    else:
        first = random.choice(female_names)

    last = random.choice(last_names)
    branch = random.choice(branches)

    students.append({
        "RollNo": i,
        "Name": f"{first} {last}",
        "Gender": gender,
        "Class": "BTech",
        "Branch": branch,
        "Section": random.choice(["A", "B", "C"]),
        "Email": f"{first.lower()}{i}@college.edu",
        "Phone": f"9{random.randint(100000000,999999999)}",
        "Courses": courses_map[branch],
        "Attendance": random.randint(40, 100),
        "Assignments": random.randint(40, 100),
        "StudyHours": random.randint(1, 6),
        "Sem1_CGPA": round(random.uniform(5, 9.5), 2),
        "Sem2_CGPA": round(random.uniform(5, 9.5), 2)
    })

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("✅ Gender matched data generated!")