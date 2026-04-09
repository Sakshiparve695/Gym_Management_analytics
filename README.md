# 🚀 Gym Management System (Backend + ETL + ML)

A backend-driven Gym Management System built using FastAPI and MySQL that supports member management, attendance tracking, analytics, and churn prediction using machine learning and ETL pipelines.

---

## 📌 Overview

This project simulates a real-world backend system. It handles operational data such as members and attendance, and transforms it into an analytics layer using an ETL pipeline. It also includes a machine learning model to predict churn risk based on user activity.

---

## ⚙️ Features

- Member Management (Add, Update, Delete, View)
- Attendance Tracking System
- Top Active Members using Heap (Priority Queue)
- Churn Prediction using Machine Learning
- ETL Pipeline for analytics processing
- Analytics API to fetch processed data

---

## 🧠 Architecture

Client / Swagger UI  
        ↓  
FastAPI Backend  
        ↓  
MySQL Database (Operational Data)  
        ↓  
ETL Pipeline (Python Script)  
        ↓  
Analytics Table (member_analytics)  

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- MySQL  
- SQL  
- scikit-learn (Logistic Regression)  
- Uvicorn  
- REST APIs  
- ETL Pipeline  
- Data Structures (Heap)  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
---

2. Install dependencies
pip install fastapi uvicorn mysql-connector-python pandas scikit-learn
3. Run the backend server
python -m uvicorn Gym_Management_System:app --reload

Open in browser:

http://127.0.0.1:8000/docs
4. Run ETL pipeline
python etl.py
---

📊 API Endpoints
Method	           Endpoint	          Description
POST	             /members	          Add new member
GET	               /members	          View all members
PUT	               /members/{id}	    Update member
DELETE	           /members/{id}	    Delete member
POST	             /attendance	      Mark attendance
GET	               /top-members	      Top active members
GET	               /churn	            Churn prediction
GET              	/analytics	        Analytics data (ETL output)

---

🔄 ETL Pipeline
Extract: Fetch attendance data from MySQL
Transform: Calculate total visits and churn risk
Load: Store processed data into member_analytics table

---

🤖 Machine Learning
Model: Logistic Regression
Feature Used: Visit frequency
Output: High or Low churn risk
Purpose: Identify inactive users for retention strategies

---

📈 Key Learnings
Built REST APIs using FastAPI
Designed and managed relational database using MySQL
Implemented ETL pipeline for data transformation
Applied data structures (Heap) for optimization
Integrated machine learning into backend system

---

💥 Future Improvements
Add authentication (JWT)
Deploy project on cloud
Build analytics dashboard
Implement CI/CD pipeline

---

👩‍💻 Author
Sakshi Parve
