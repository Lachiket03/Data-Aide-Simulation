# 📊 Data Aide Simulation Project

This project simulates the daily tasks of a **Data Aide** working in an after-school program, focusing on **data cleaning**, **quality checks**, and **reporting** using real-world tools like Python, Pandas, and Streamlit.

---

## 🧩 Project Overview

### 🎯 Goal
To build a mini-portfolio project that mirrors what a data aide might do in an educational or nonprofit setting: track attendance, verify student data, and create basic reports.

---

## 🗃️ Dataset

A synthetic dataset of 50 students was generated using Python’s Faker library. Fields include:

- `Student_ID`
- `Name`
- `Age` (7–14)
- `Grade` (1–8)
- `Program` (STEM, Arts, Sports, Reading)
- `Consent_Given` (Yes/No)
- `Attendance_Dates` (randomized list of dates in June)

📁 Located in: `/data/after_school_data.csv`

---

## 🔍 Features

### ✅ Data Cleaning Script (`clean_data.py`)
Performs the following checks:
- Missing values
- Duplicate entries
- Age-grade mismatches
- Consent form verification
- Attendance absences (>3)
- Form completeness score

📄 Output: `after_school_data_cleaned.csv`

---

### 🖥️ Streamlit App (`app.py`)

An interactive dashboard where users can:

- Upload raw CSV data
- View error summaries and charts
- Identify problematic records
- Download the cleaned version of the data

📸 Features:
- Attendance histograms
- Program distribution bar chart
- Dynamic metrics for data quality

---

## 🛠️ Tools Used

| Purpose              | Tool          |
|----------------------|---------------|
| Data Generation      | Python, Faker |
| Cleaning & QC        | Pandas        |
| Dashboard & Reports  | Streamlit     |
| Charts               | Matplotlib    |
| Versioning           | Git + GitHub  |

---

## 📁 Folder Structure

data-aide-sim/

│

├── data/

│ └── after_school_data.csv

├── scripts/

│ └── clean_data.py

├── reports/

│ └── cleaned_data_sample.csv

├── app.py

└── README.md
