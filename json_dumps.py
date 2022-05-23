import json
python_dict_obj = {
    "Avengers": [
        {
            "Name": "Tony stark",
            "also known as": "Iron man",
            "Abilities": [
                "Genius",
                "Billionaire",
                "Playboy",
                "Philanthropist"
            ]
        },
        {
            "Name": "Peter parker",
            "also known as": "Spider man",
            "Abilities": [
                "Spider web",
                "Spidy sense"
            ]
        }
    ]
}
print(type(python_dict_obj))
var = json.dumps(python_dict_obj)
print(var)
print(type(var))