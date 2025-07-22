# 💼 Job Salary Prediction App

This is a Streamlit web app that predicts the **salary for a job role** based on various features such as job title, location, employment type, and company rating. The model is trained on a dataset named **`Salary_Dataset_with_Extra_Features.csv`** using the **XGBoost regression algorithm**.

---

## 🚀 Features

- 🔮 Predict salary based on:
  - Company rating
  - Job title
  - Company name
  - Location
  - Employment status
  - Reported salaries
  - Job role & seniority
- 🧠 Trained with **XGBoost Regressor**
- 📊 Shows predicted salary in ₹ (INR)
- 🧮 Includes job seniority extraction logic
- ✅ Lightweight and easy to deploy using **Streamlit**

---

## 🧠 Model Overview

- **Algorithm**: XGBoost Regressor
- **Problem Type**: Regression
- **Training Dataset**: `Salary_Dataset_with_Extra_Features.csv`

### 📈 Evaluation Metrics:
- **Mean Absolute Error (MAE)**: ₹267,829.84  
- **R² Score**: 0.1612

> Target variable is log-transformed during training. Final output is converted back using exponential function.

---

## 📁 Input Features

| Feature             | Description                             |
|---------------------|-----------------------------------------|
| Rating              | Company rating (1.0 to 5.0)             |
| Company Name        | Name of the company                     |
| Job Title           | Role title (e.g., Software Engineer)    |
| Salaries Reported   | Number of salaries reported             |
| Location            | Job location                            |
| Employment Status   | Full Time / Part Time / Contract / Intern |
| Job Roles           | Web, Android, Data Science, DevOps, etc.|
| Job Seniority       | Extracted from job title                |

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- XGBoost
- Streamlit
- Joblib

---

## ⚙️ How to Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/job-salary-prediction-app.git
cd job-salary-prediction-app
