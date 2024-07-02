import requests
import json
<<<<<<< HEAD
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/api/students', methods=['GET'])
def get_students():
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTk4NTMxNTIsInN1YiI6ImZ6YTIifQ.x9acfzRBL0esvwKUDRQ5ucDZbBr7uBhraOvCltauEso'  # Updated API key
    url = 'https://yalies.io/api/people'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        "page": 1,
        "page_size": 100
    }
    
    try:
        print("Sending request to API...")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print(f"Payload: {json.dumps(payload)}")

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

        if response.status_code == 200:
            students = response.json()
            print(f"Parsed students data: {json.dumps(students, indent=4)}")  # Log the full JSON response
            if not students:
                print("Error: No students data returned")
                return jsonify({"error": "No students data returned"}), 500

            student_data = []
            for student in students:
                student_info = {
                    "Name": f"{student.get('first_name', '')} {student.get('last_name', '')}",
                    "Email": student.get('email', 'N/A'),
                    "College": student.get('college', 'N/A'),
                    "Year": student.get('year', 'N/A'),
                    "Major": student.get('major', 'N/A'),
                    "Pronouns": student.get('pronouns', 'N/A'),
                    "Address": student.get('address', 'N/A')
                }
                student_data.append(student_info)
            return jsonify(student_data)
        else:
            print("Error: Failed to retrieve data from API")
            return jsonify({"error": f"Failed to retrieve data from API. Status code: {response.status_code}, Response: {response.content.decode()}"}), response.status_code
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": f"Exception occurred: {str(e)}"}), 500

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/script.js')
def serve_script():
    return send_from_directory('.', 'script.js')

@app.route('/style.css')
def serve_style():
    return send_from_directory('.', 'style.css')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
import pandas as pd
import sqlalchemy as db

# Your API key
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTk3MDM5MzMsInN1YiI6ImZ6YTIifQ.E29HeBtftRvGdTbLNRZou8A5JnqIJ7YOtdv2GbhP9XA'

# The URL for the POST request
url = 'https://yalies.io/api/people'

# The headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Simplified payload
payload = {
    "query": "",
    "page": 1,
    "page_size": 10
}

# Sending the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    students = response.json()
    
    # Parse students into a dictionary
    student_data = []
    for student in students:
        student_info = {
            "Name": f"{student.get('first_name')} {student.get('last_name')}",
            "Email": student.get('email'),
            "College": student.get('college'),
            "Year": student.get('year'),
            "Major": student.get('major'),
            "Pronouns": student.get('pronouns'),
            "Address": student.get('address')
        }
        student_data.append(student_info)
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame.from_dict(student_data)
    
    # Create an engine object
    engine = db.create_engine('sqlite:///students.db')
    
    # Create and send SQL table from your DataFrame
    df.to_sql('students', con=engine, if_exists='replace', index=False)
    
    # Write a query and print out the results
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM students;")).fetchall()
        result_df = pd.DataFrame(query_result)
        print(result_df)
else:
    print(f"Failed to retrieve data: {response.status_code}")
>>>>>>> origin/main
