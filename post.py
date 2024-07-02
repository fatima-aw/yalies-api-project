import requests

# Define the URL for the POST request
url = 'https://jsonplaceholder.typicode.com/posts'

# Define the data to be sent in the POST request
data = {
    'title': 'Special Agent',
    'body': 'Leroy Jethro Gibbs',
    'userId': '1'
}

# Send the POST request
response = requests.post(url, data=data)

# Print out the status code of the response
print(response.status_code)

# Print out the response in JSON format
print(response.json())
