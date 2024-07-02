import requests

# Get text from the user to send to the API
user_input = input("Enter text for sentiment analysis: ")

# Prepare the data to be sent in the POST request
myobj = {'text': user_input}

# Define the API URL
url = 'http://text-processing.com/api/sentiment/'

# Send the POST request
response = requests.post(url, data=myobj)

# Print the status code of the response
print("Status Code:", response.status_code)

# Print the response in JSON format
print("Response JSON:", response.json())
