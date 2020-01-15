#!/usr/bin/env python3
import requests
import pprint

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


r = requests.get('https://api.fortnitetracker.com/v1/store', headers={'TRN-Api-Key': '0946c1e7-cd3d-4dd9-b294-54d2ff7885d1'})

# pprint.pprint(r.status_code)
# jprint(r.json())

data = r.json()

for x in data:
    print("Name: " + x["name"])
    print("Cost: " + str(x["vBucks"]) + " vBucks")
    print("URL: " + x["imageUrl"])
    print("")
