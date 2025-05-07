### Remote REST API Call to trigger alarm
import requests
server="http://localhost:5050"
headers = {"Content-Type": "application/json","Authorization": "Bearer my-test-token"}
response = requests.post(server+"/create",headers=headers,data=json.dumps({"action":"play sound"}))
