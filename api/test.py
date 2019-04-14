import requests
import json

# URL = "http://192.168.0.4:5010/delete_ip"
# headers = {'Content-type':'application/json'}

# #data = {"email":"rashmipawar921@gmail.com"}
# data = {"email":"rashmipawar921@gmail.com","raspberry_id":1,"nodemcu_id":1,"nodemcu_ip":"192.254.152.169","raspberry_ip":"192.254.152.165","today_date":"2019-03-18"}
# json_data = json.dumps(data)

# r = requests.get(url=URL, json = json_data, headers= headers)
# print(r.json)
# print(r.text)

URL = "http://192.168.0.4:5010/select_mois_data"
headers = {'Content-type':'application/json'}

#data = {"email":"rashmipawar921@gmail.com"}
data = {"email":"rashmipawar921@gmail.com","raspberry_id":1,"nodemcu_id":1,"nodemcu_ip":"192.254.152.164","raspberry_ip":"192.254.152.165","today_date":"2019-03-18"}
json_data = json.dumps(data)

r = requests.get(url=URL, json = json_data, headers= headers)
print(r.json)
print(r.text)