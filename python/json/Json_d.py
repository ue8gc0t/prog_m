import json

data = {
    "x":[1,2,3,4],
    "y":[4,3,2,1], 
    "z":{
            "a":1,
            "b":2
        }
    
}

with open("json.json", "w") as write_file:
    json.dump(data, write_file, sort_keys=True, indent=4)