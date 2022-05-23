import json
# serialization
employee = {"name" : "Madhav",
            'age':35,
            'salary':15000,
             'married':False,
            'a':None,}
json_string = json.dumps(employee,indent=4)
print(json_string)

with open('emp.json','w') as f :
    json.dump(employee,f)

# deserialization
employee2 = ''' {
    "name": "Madhav",
    "age": 35,
    "salary": 15000,
    "married": false,
    "a": null }'''

python_string = json.loads(employee2)

print(python_string)
for k,v in python_string.items():
    print('{}:{}'.format(k,v))

# deserialization from json file
employee2 = ''' 
    {"name": "Madhav",
    "age": 35,
    "salary": 15000,
    "married": false,
    "a": null } '''


with open('emp.json','r') as f:
    python_string = json.load(f)

print(python_string,"as offfffffffffffffffffffffffffffffffff")
for k,v in python_string.items():
    print('{}:{}'.format(k,v))