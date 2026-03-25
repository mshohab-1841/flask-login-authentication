#backend
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ls96qe_2000",
        database="details"
    )

    if db.is_connected():
        print("✅ Connected to MySQL successfully!")

except Exception as e:
    print("❌ Error:", e)