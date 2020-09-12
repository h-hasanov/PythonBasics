import requests
from pprint import pprint

req = requests.get("http://google.co.uk")

req = requests.get("http://date.jsontest.com")
pprint(req.json())

jsonData = req.json()
print(str(jsonData))
req = requests.post("http://validate.jsontest.com?json="+str(jsonData))
print(req.content)

def generalizePost(url, jsonData):
    headers = {"content-type": "application/json"}
    cookies = {"cookie_1": "some-cookie value"}
    response1 = requests.post(url, json=jsonData, headers=headers, cookies=cookies)
    return response1

t = generalizePost(url="http://validate.jsontest.com", jsonData=jsonData)
print(t.content)