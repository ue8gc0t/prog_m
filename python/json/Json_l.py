import json

with open("json.json", "r") as read_file:
    Json = json.load(read_file)
    
print(Json)
print(Json["x"])
print(Json["z"]["a"])