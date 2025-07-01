import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
random.seed(42)

# Settings
num_students = 50
programs = ['STEM', 'Arts', 'Sports', 'Reading']
attendance_pool = pd.date_range(start='2025-06-01', end='2025-06-28').tolist()

# Helper: Age ↔ Grade mapping (roughly)
def age_grade_pair():
    age = random.randint(7, 14)
    grade = age - 6
    return age, grade

# Generate students
students = []
for i in range(1, num_students + 1):
    student_id = f"STU{i:03}"
    name = fake.name()
    age, grade = age_grade_pair()
    program = random.choice(programs)
    consent = random.choices(['Yes', 'No'], weights=[0.9, 0.1])[0]
    attendance = sorted(random.sample(attendance_pool, random.randint(10, 20)))
    attendance_str = ','.join([d.strftime('%Y-%m-%d') for d in attendance])

    students.append({
        "Student_ID": student_id,
        "Name": name,
        "Age": age,
        "Grade": grade,
        "Program": program,
        "Consent_Given": consent,
        "Attendance_Dates": attendance_str
    })

# Convert to DataFrame
df = pd.DataFrame(students)

# Save to CSV
df.to_csv("after_school_data.csv", index=False)
print("✅ Dataset generated: after_school_data.csv")
