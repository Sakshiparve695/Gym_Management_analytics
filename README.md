# 🏋️ AI-Driven Gym Analytics & Churn Prediction Platform

## 🚀 Overview

A backend-driven analytics platform built using **FastAPI** that manages gym operations, processes attendance data, and predicts customer churn using machine learning.

The system also provides **data visualization insights** and is fully **containerized using Docker** for consistent deployment.

---

## ✨ Key Features

* 🔧 RESTful API development using FastAPI
* 🗄️ MySQL database integration for structured data management
* 📊 Data processing and analytics using Pandas
* 🤖 Churn prediction using Scikit-learn (Logistic Regression)
* 📈 Visualization endpoint for attendance insights
* 📦 Docker-based containerization for portability and scalability
* ⚡ Efficient query handling and real-time data processing

---

## 📊 API Endpoints

| Endpoint                    | Description                               |
| --------------------------- | ----------------------------------------- |
| `/members`                  | Add, update, view, delete members         |
| `/attendance`               | Record gym attendance                     |
| `/top-members`              | Get top active members (Heap-based logic) |
| `/churn`                    | Predict churn risk using ML model         |
| `/insights`                 | Generate gym usage insights               |
| `/analytics`                | View processed analytics data             |
| `/visualization/attendance` | View attendance chart 📊                  |

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **Database:** MySQL
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Visualization:** Matplotlib
* **Deployment:** Docker

---

## 🐳 Docker Setup

### 1. Build Docker Image

```
docker build -t gym-app .
```

### 2. Run Container

```
docker run -p 8000:8000 gym-app
```

### 3. Access API

```
http://localhost:8000/docs
```

---

## ⚠️ Important Note

While using Docker:

* Replace `localhost` with `host.docker.internal` for MySQL connection

---

## 🧠 Challenges & Learnings

* Resolved Docker networking issue (localhost vs container networking)
* Designed scalable API architecture
* Integrated ML model into backend pipeline
* Built analytics-ready data processing workflows

---

## 📌 Future Enhancements

* Add authentication (JWT-based security)
* Build interactive dashboard (Streamlit / Plotly)
* Use Docker Compose for multi-container setup (App + DB)
* Deploy on cloud (AWS / Render)

---

## 👩‍💻 Author

**Sakshi Parve**

---

## ⭐ If you like this project, give it a star!
