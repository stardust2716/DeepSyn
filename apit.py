import requests
import json

selected_text = 'high' 
url = 'http://localhost/v1/chat-messages'

headers = {
    'Authorization': 'Bearer app-wzs5nVWkiTZPwmk2qUp8Xmz4',
    'Content-Type': 'application/json;charset=utf-8',
}
data = {
    "inputs": {},
    'query': selected_text ,
    "response_mode": "blocking",
    "user": "abc-123"
}
response = requests.post(url, headers=headers, data=json.dumps(data))          
data=response.content.decode('utf-8')
json_data = json.loads(data,strict=False)
#print(json_data)
answerstr = json_data.get('answer')
print(answerstr)