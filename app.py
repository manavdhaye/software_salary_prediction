import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("xgboost_salary_model.pkl")

st.title("Job Salary Prediction App")
st.markdown("Enter job details below to predict the salary:")

rating = st.slider("Company Rating", 1.0, 5.0, 4.0, step=0.1)
company_name = st.text_input("Company Name", "Google")
job_title = st.text_input("Job Title", "Software Engineer")
salaries_reported = st.number_input("Salaries Reported", 1, 100, 3)
location = st.text_input("Location", "Bangalore")
employment_status = st.selectbox("Employment Status", ["Full Time", "Part Time", "Contract", "Intern"])
job_roles = st.selectbox("Job Role", ["Web", "Android", "Data Science", "DevOps", "Cloud", "Other"])

def extract_seniority(title):
    title = title.lower()
    if "intern" in title:
        return "Intern"
    elif "senior" in title or "sr" in title:
        return "Senior"
    elif "lead" in title or "head" in title:
        return "Lead"
    elif "associate" in title:
        return "Associate"
    elif "junior" in title:
        return "Junior"
    else:
        return "Mid"

job_seniority = extract_seniority(job_title)

if st.button("Predict Salary"):
    # Create DataFrame
    input_data = pd.DataFrame({
    'Rating': [rating],
    'Company Name': [company_name],
    'Job Title': [job_title],
    'Salaries Reported': [salaries_reported],
    'Location': [location],
    'Employment Status': [employment_status],
    'Job Roles': [job_roles],
    'Job Seniority': [job_seniority]
    })

# Predict
    try:
        log_salary_pred = model.predict(input_data)
        predicted_salary = np.expm1(log_salary_pred[0])
        st.success(f"Predicted Salary: ₹{predicted_salary:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
