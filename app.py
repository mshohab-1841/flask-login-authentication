from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="details"
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return "Backend Running!"

# 🔹 REGISTER
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']

    # ❌ prevent empty values
    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "User already exists"}), 400

    cursor.execute(
        "INSERT INTO users (email, password) VALUES (%s, %s)",
        (email, password)
    )
    db.commit()

    return jsonify({"message": "Registered successfully"})

# 🔹 LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
