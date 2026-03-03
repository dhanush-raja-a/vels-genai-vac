# Day 03: REST APIs and JSON Parsing

import requests
import json

# 1. Understanding REST APIs
# We use the 'requests' library to fetch data from the web.
# A common API is the JSONPlaceholder, which provides fake data for testing.

print("--- Fetching data from a REST API ---")
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# Status code 200 means success
if response.status_code == 200:
    print(f"Success! Status Code: {response.status_code}")
    
    # 2. JSON Parsing
    # Data from APIs often comes in JSON format (which looks like a Python dictionary).
    data = response.json()
    print("\nParsed JSON Data:")
    print(data)
    
    # Accessing specific fields
    title = data.get('title')
    completed = data.get('completed')
    print(f"\nTitle: {title}")
    print(f"Is Completed: {completed}")

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")

# 3. Converting Python objects to JSON
print("\n--- Converting Dictionary to JSON String ---")
user_info = {
    "name": "Dhanush",
    "topic": "Python NLP",
    "day": 3
}

json_string = json.dumps(user_info, indent=4)
print(json_string)
