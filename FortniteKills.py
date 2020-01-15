import requests
import pprint

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("What do you play on? (pc, xbl, psn)")
type = input()

print("What is your Username: ")
name = input()

r = requests.get('https://api.fortnitetracker.com/v1/profile/' + type + '/' + name, headers={'TRN-Api-Key': '0946c1e7-cd3d-4dd9-b294-54d2ff7885d1'})

# pprint.pprint(r.status_code)
# jprint(r.json())

data = r.json()

print("")
print("Solo Kills: ")
print(data["stats"]["p2"]["kills"]["displayValue"])
print("")


print("Duo Kills: ")
print(data["stats"]["p10"]["kills"]["displayValue"])
print("")

print("Squad Kills: ")
print(data["stats"]["p9"]["kills"]["displayValue"])


