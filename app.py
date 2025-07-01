import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Aide App", layout="wide")

st.title("📊 After-School Program Data Cleaner & Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df.head())

    # Add calculated columns
    df["Expected_Grade"] = df["Age"] - 6
    df["Num_Attendance_Days"] = df["Attendance_Dates"].apply(lambda x: len(str(x).split(",")))
    df["Absences"] = 28 - df["Num_Attendance_Days"]
    df["Completeness (%)"] = df[["Name", "Age", "Grade", "Program", "Consent_Given", "Attendance_Dates"]].notnull().sum(axis=1) / 6 * 100

    # Section: Errors and Quality Checks
    st.markdown("## 🚨 Data Quality Checks")

    col1, col2, col3 = st.columns(3)

    with col1:
        duplicates = df[df.duplicated(subset=["Student_ID"])]
        st.metric("Duplicates", len(duplicates))
        if not duplicates.empty:
            st.write("Duplicate Records:")
            st.dataframe(duplicates)

    with col2:
        no_consent = df[df["Consent_Given"] != "Yes"]
        st.metric("Missing Consent", len(no_consent))
        if not no_consent.empty:
            st.write("Students without Consent:")
            st.dataframe(no_consent[["Student_ID", "Name", "Consent_Given"]])

    with col3:
        mismatches = df[df["Grade"] != df["Expected_Grade"]]
        st.metric("Age-Grade Mismatches", len(mismatches))
        if not mismatches.empty:
            st.write("Mismatches:")
            st.dataframe(mismatches[["Student_ID", "Age", "Grade", "Expected_Grade"]])

    st.markdown("---")

    # Section: Attendance Summary
    st.markdown("## 📉 Attendance Check")
    low_attendance = df[df["Absences"] > 3]
    st.write(f"Students with >3 absences: {len(low_attendance)}")
    st.dataframe(low_attendance[["Student_ID", "Name", "Absences"]])

    # Charts
    st.markdown("## 📊 Visual Reports")

    col4, col5 = st.columns(2)

    with col4:
        program_counts = df["Program"].value_counts()
        st.bar_chart(program_counts)

    with col5:
        st.write("Attendance Histogram")
        st.bar_chart(df["Num_Attendance_Days"])

    # Cleaned Data Preview
    st.markdown("## ✅ Cleaned Data Preview")
    df_cleaned = df.drop(columns=["Expected_Grade"])
    st.dataframe(df_cleaned)

    # Download option
    csv = df_cleaned.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Cleaned CSV", data=csv, file_name="cleaned_data.csv", mime='text/csv')
