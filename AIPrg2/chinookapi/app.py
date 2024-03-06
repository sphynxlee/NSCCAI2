from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def execute_query(query, params=None, fetchone=False):
    connection = sqlite3.connect("chinook.sqlite")
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    connection.commit()
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    connection.close()
    return result

@app.get("/")
def api_intro():
    return("Hey there! Welcome to my sqlite backed API.")

@app.get("/customers")
def get_customers():
    query = "SELECT * FROM customers"
    result = execute_query(query)
    return jsonify(result)

app.run(debug=True)