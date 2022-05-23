import json

Json_data = {
    "Avengers": [

        {
            "Name": "Tony stark",
            "also known as": "Iron man",
            "Abilities": ["Genius", "Billionaire",
                          "Playboy", "Philanthropist"]
        },

        {
            "Name": "Peter parker",
            "also known as": "Spider man",
            "Abilities": ["Spider web", "Spidy sense"]
        }
    ]
}

with open("sample.json",'w') as p:
    json.dump(Json_data,p,indent=4)
print(type(Json_data))
