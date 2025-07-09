import json


#python Object -> json String
"""
person = {
    "name": "Alin",
    "age": 25,
    "occupation": "Software Developer",
    "skills": ["Python", "JavaScript", "Machine Learning"],
    "location": "Bangladesh",
    "is_student": False
}

x=json.dumps(person,indent=4)
print(x)


# json String  -> python Object 


personJSON = '{"name": "John", "age": 30, "city": "New York", "is_student": true, "is_employed": false, "skills": ["Python", "JavaScript", "SQL"]}'

personOBJ = json.loads(personJSON)

print(personOBJ)



person = {
    "name": "Alin",
    "age": 25,
    "occupation": "Software Developer",
    "skills": ["Python", "JavaScript", "Machine Learning"],
    "location": "Bangladesh",
    "is_student": False
}

with open("person.json", "w") as personJSONFile:
    json.dump(person, personJSONFile,indent=4)

"""