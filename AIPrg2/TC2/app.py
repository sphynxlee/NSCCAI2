# create a basic flask app

from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

# 1. Create a Flask app. Add an endpoint at the root (/) of the service that returns the string, "Hyperparameters are still a mystery to me!"
@app.get("/")
def api_intro():
    return("Hyperparameters are still a mystery to me!")

# 2. Add the Chinook sqlite DB to your project. Select a table (not customers) from the DB. Write an endpoint at /<table_name> that returns all of the rows from your chosen table.
@app.get("/employees")
def get_customers():
    query = "SELECT * FROM employees"
    result = execute_query(query)
    return jsonify(result)

# Professor, I will do Step 4 first, then come back to Step 3. (Due to my OCD)
# 4. Create a final endpoint at /<table_name> that enables a user of your API to add a row/record to the table. Use an appropriate HTTP verb.
# I use mock data for the new employee.
# {"FirstName": "Haidun", "LastName": "Li"}
@app.post("/addEmployees")
def add_employee():
    person = request.get_json()
    query = '''INSERT INTO employees (LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email)'''
    query += ''' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    params = (person["LastName"], person["FirstName"], 'Staff', 6, "1981-12-22", "2023-09-01", "200 Broad St", "Halifax", "NS", "Canada", "B4B 0T4", 7828823107, 7828823107, "kaiton.ri@gmail.com")
    result = execute_query(query, params)
    return jsonify(result)

# 3. Create another endpoint at /<table_name> that enables a user of your API to update a row/record in your chosen table. Use an appropriate HTTP verb and call me over to demonstrate your endpoint working using Insomnia or POSTman or curl or whatever other client you want to use.
@app.post("/updateEmployees")
def update_employee():
    person = request.get_json()
    query = '''UPDATE employees SET FirstName = ?, LastName = ? WHERE EmployeeId = ?'''
    params = (person["FirstName"], person["LastName"], 9)
    result = execute_query(query, params)
    return jsonify(result)

# 5. To demonstrate that your endpoint from step 4 works, write an HTML form that includes the required fields and, on submission of the form, calls the step 4 endpoint and passes along the data.
# I will do this in the step5.html file.


if __name__ == '__main__':
    app.run(debug=True)