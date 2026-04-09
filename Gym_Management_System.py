from fastapi import FastAPI, HTTPException
import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Gym Management API is running 🚀"}

# -------- DB CONNECTION --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakshi@123",
    database="sakshi_project_db"
)
cursor = conn.cursor()

# -------- ADD MEMBER --------
@app.post("/members")
def add_member(name: str, age: int, phone: str, email: str, plan: int):
    try:
        query = "INSERT INTO members(name, age, phone, email, plan) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (name, age, phone, email, plan))
        conn.commit()
        return {"message": "Member added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- VIEW MEMBERS --------
@app.get("/members")
def view_members():
    try:
        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()
        return {"members": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- UPDATE MEMBER --------
@app.put("/members/{member_id}")
def update_member(member_id: int, name: str, age: int, phone: str, email: str, plan: int):
    try:
        query = """
        UPDATE members
        SET name=%s, age=%s, phone=%s, email=%s, plan=%s
        WHERE member_id=%s
        """
        cursor.execute(query, (name, age, phone, email, plan, member_id))
        conn.commit()
        return {"message": "Member updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- DELETE MEMBER --------
@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    try:
        cursor.execute("DELETE FROM members WHERE member_id=%s", (member_id,))
        conn.commit()
        return {"message": "Member deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- MARK ATTENDANCE --------
@app.post("/attendance")
def mark_attendance(member_id: int, visit_date: str):
    try:
        query = "INSERT INTO attendance(member_id, visit_date) VALUES (%s,%s)"
        cursor.execute(query, (member_id, visit_date))
        conn.commit()
        return {"message": "Attendance recorded"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- TOP ACTIVE MEMBERS (DSA: Heap) --------
@app.get("/top-members")
def top_active_members():
    try:
        cursor.execute("""
            SELECT member_id, COUNT(*) AS visits
            FROM attendance
            GROUP BY member_id
        """)
        rows = cursor.fetchall()

        import heapq
        top5 = heapq.nlargest(5, rows, key=lambda x: x[1])

        return {"top_members": top5}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- CHURN PREDICTION --------
@app.get("/churn")
def churn_prediction():
    try:
        cursor.execute("""
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
        """)
        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=["member_id","visits"])
        df["churn"] = df["visits"].apply(lambda x: 1 if x < 5 else 0)

        X = df[["visits"]]
        y = df["churn"]

        if len(set(y)) < 2:
            return {"message": "Not enough data for prediction"}

        model = LogisticRegression()
        model.fit(X, y)

        df["prediction"] = model.predict(X)

        result = []
        for _, row in df.iterrows():
            result.append({
                "member_id": int(row["member_id"]),
                "risk": "HIGH" if row["prediction"] == 1 else "LOW"
            })

        return {"churn_analysis": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------- GYM INSIGHTS --------
@app.get("/insights")
def gym_insights():
    try:
        cursor.execute("""
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
        """)
        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=["member_id","visits"])

        avg_visits = df["visits"].mean()

        insights = []
        for _, row in df.iterrows():
            if row["visits"] >= 10:
                status = "Highly Active"
            elif row["visits"] < 3:
                status = "Low Attendance"
            else:
                status = "Moderate"

            insights.append({
                "member_id": int(row["member_id"]),
                "visits": int(row["visits"]),
                "status": status
            })

        return {
            "average_visits": round(avg_visits, 2),
            "insights": insights
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/analytics")
def get_analytics():
    cursor.execute("SELECT * FROM member_analytics")
    return {"analytics": cursor.fetchall()}