import requests

# Employ GET Request
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Print status code
print(response.status_code)

# Print first 5 names in people dictionary
for person in data['people'][:5]:
    print(person['name'])
