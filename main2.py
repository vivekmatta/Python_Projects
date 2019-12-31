import requests
import pprint
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# pprint.pprint(r.status_code)
# jprint(r.json())

data = r.json()

print("Current Price: ")
print(data["bpi"]["USD"]["rate_float"])

print("")

print("Time")
print(data["time"]["updated"])


