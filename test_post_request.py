import requests
import json

# Your API key
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTk3MDM5MzMsInN1YiI6ImZ6YTIifQ.E29HeBtftRvGdTbLNRZou8A5JnqIJ7YOtdv2GbhP9XA'

# The URL for the POST request
url = 'https://yalies.io/api/people'

# The headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# The payload for the request
payload = {
    "query": "Fatima",  # Empty query to get all data
    "page": 1,
    "page_size": 10
}

# Sending the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Printing the response
print(response.status_code)
print(response.json())

