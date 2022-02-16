import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
# print(response)
# print(response.headers)
# print(response.headers.get('Server'))
# print(response.cookies)

json_response = json.loads(response.text)
print(json_response)

id = jsonpath.jsonpath(json_response,'data[3].id')
print(id)