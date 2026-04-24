import random

def predict_student(student):

    attendance = student["Attendance"]
    assignments = student["Assignments"]
    study_hours = student["StudyHours"]
    sem1 = student["Sem1_CGPA"]
    sem2 = student["Sem2_CGPA"]

    # Weighted score
    score = (
        attendance * 0.2 +
        assignments * 0.2 +
        study_hours * 10 * 0.2 +
        sem1 * 10 * 0.2 +
        sem2 * 10 * 0.2
    )

    if score >= 70:
        result = "Pass"
        predicted_cgpa = round((sem1 + sem2)/2 + 0.5, 2)
    elif score >= 55:
        result = "Borderline"
        predicted_cgpa = round((sem1 + sem2)/2, 2)
    else:
        result = "Fail"
        predicted_cgpa = round((sem1 + sem2)/2 - 1, 2)

    # Attendance status
    if attendance >= 75:
        status = "Satisfactory"
    elif attendance >= 65:
        status = "Condonation"
    elif attendance >= 50:
        status = "Shortage"
    else:
        status = "Detained"

    # Study recommendation
    if result == "Fail":
        study = 5
    elif result == "Borderline":
        study = 3
    else:
        study = 2

    return result, status, study, predicted_cgpa