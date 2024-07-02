import requests
import json
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
