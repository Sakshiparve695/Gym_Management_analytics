import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakshi@123",
    database="sakshi_project_db"
)

cursor = conn.cursor()

def run_etl():
    print("Running ETL...")

    cursor.execute("""
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
    """)
    data = cursor.fetchall()

    processed = []
    for row in data:
        member_id = row[0]
        visits = row[1]
        churn = 1 if visits < 5 else 0
        processed.append((member_id, visits, churn))

    for row in processed:
        cursor.execute("""
            INSERT INTO member_analytics (member_id, total_visits, churn_risk)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                total_visits = VALUES(total_visits),
                churn_risk = VALUES(churn_risk)
        """, row)

    conn.commit()
    print("ETL completed")

if __name__ == "__main__":
    run_etl()