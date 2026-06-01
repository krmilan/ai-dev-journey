import json

# Python dictionary
person = {
    "name": "Alex",
    "skills": ["Python", "FastAPI", "OpenAI"],
    "experience": 0,
    "looking_for_job": True
}

# Dictionary → JSON string (for sending over internet)
json_string = json.dumps(person, indent=2)
print("AS JSON STRING:")
print(json_string)
print(type(json_string))  # <class 'str'>

# JSON string → Dictionary (for using in code)
parsed_back = json.loads(json_string)
print("\nPARSED BACK TO DICT:")
print(parsed_back["skills"])
print(type(parsed_back))  # <class 'dict'>

# Save JSON to a file
with open("person.json", "w") as f:
    json.dump(person, f, indent=2)
print("\nSaved to person.json")

# Read JSON from a file
with open("person.json", "r") as f:
    loaded = json.load(f)
print(f"Loaded from file: {loaded['name']}")