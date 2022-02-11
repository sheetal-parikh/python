import json
import requests
print("Hello")
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(requests.check_compatibility:/response.text)