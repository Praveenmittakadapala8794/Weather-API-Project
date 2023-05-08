import requests
import json
city = input("enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=66b96ec19071449a911192655230704&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_f"]
print(w)
