import pandas as pd

# Load data
df = pd.read_csv("after_school_data.csv")

# --- 1. Check for missing values ---
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# --- 2. Check for duplicate Student_IDs ---
duplicates = df[df.duplicated(subset=["Student_ID"])]
print(f"\n🔁 Duplicate Entries: {len(duplicates)}")
if not duplicates.empty:
    print(duplicates)

# --- 3. Check Age vs Grade logic ---
print("\n⚠️ Age-Grade Mismatches (expected Grade = Age - 6):")
df["Expected_Grade"] = df["Age"] - 6
mismatches = df[df["Grade"] != df["Expected_Grade"]]
print(mismatches[["Student_ID", "Age", "Grade", "Expected_Grade"]])

# --- 4. Check Consent Missing or No ---
print("\n🚫 Students without Consent:")
no_consent = df[df["Consent_Given"] != "Yes"]
print(no_consent[["Student_ID", "Name", "Consent_Given"]])

# --- 5. Attendance check: >3 days missed ---
print("\n📉 Students with >3 absences:")
df["Num_Attendance_Days"] = df["Attendance_Dates"].apply(lambda x: len(str(x).split(",")))
df["Absences"] = 28 - df["Num_Attendance_Days"]  # Total June days: 28
low_attendance = df[df["Absences"] > 3]
print(low_attendance[["Student_ID", "Name", "Absences"]])

# --- 6. Intake form completeness score ---
print("\n✅ Form Completeness (% filled):")
required_cols = ["Name", "Age", "Grade", "Program", "Consent_Given", "Attendance_Dates"]
df["Completeness (%)"] = df[required_cols].notnull().sum(axis=1) / len(required_cols) * 100
print(df[["Student_ID", "Completeness (%)"]].head())

# --- 7. Save cleaned data ---
df_cleaned = df.drop(columns=["Expected_Grade"])
df_cleaned.to_csv("after_school_data_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to: after_school_data_cleaned.csv")
