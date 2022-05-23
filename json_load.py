import json

with open("sample.json","r") as read_it:
    data = json.load(read_it)
    print(data)
    print(type(data))

