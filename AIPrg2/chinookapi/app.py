# create a basic flask app
# create a GET endpoint that returns all customers from the chinook database
# create a POST endpoint that adds a new customer to the chinook database

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

@app.post("/addcustomers")
def add_customer():
    person = request.get_json()
    query = '''INSERT INTO customers (FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId)'''
    query += ''' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    params = (person["FirstName"], person["LastName"], 'NSCC', '5685 Leeds St', 'Halifax', 'NS', 'Canada', 'B3K 2T3', 9024916722, 9024916722, 'someone@nscc.ca', 2)
    result = execute_query(query, params)
    return jsonify(result)

app.run(debug=True)