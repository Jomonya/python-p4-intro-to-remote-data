import requests
import json
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"
response = requests.get(url)
json.loads(response.content)
print(response.text)
print(response.content)