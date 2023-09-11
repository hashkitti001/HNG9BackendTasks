import requests

# Create a new person
data = {"name": "Abel Tesfaye", "age": 23}
response = requests.post("http://127.0.0.1:5000/persons", json=data)
print(response.json())

# Get details of a person
response = requests.get("http://127.0.0.1:5000/persons/Abel Tesfaye")
print(response.json())

# Update the age of a person
data = {"age": 35}
response = requests.put("http://127.0.0.1:5000/persons/", json=data)
print(response.json())

# Delete a person
response = requests.delete("http://127.0.0.1:5000/persons/Mia Khalifa")
print(response.json())
