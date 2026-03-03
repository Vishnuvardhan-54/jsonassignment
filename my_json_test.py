import json
user_profile={
    "name":"vishnu",
    "age":21,
    "email":"vishnu@gmail.com",
    "is_active":True,
    "skills":["python","ML","NumPy","pandas"]
}

details=json.dumps(user_profile,indent=4)
print(details)
print("-"*60)

#TASK 2
information= {"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}
info_json=json.dumps(information,indent=4)
info=json.loads(info_json)

print("Username: ",info["data"]["username"])
print("Score: ",info["data"]["score"])

print(f"A message: User {info["data"]["username"]} scored {info["data"]["score"]}")
print("-"*60)

#TASK 3

json_data = '''
{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
'''
data = json.loads(json_data)

city = data["address"]["city"]
zip_code = data["address"]["zip"]

print("City:", city)
print("Zip Code:", zip_code)

# Add new key inside address
data["address"]["country"] = "India"
updated_json = json.dumps(data, indent=4)

print("\nUpdated JSON:")
print(updated_json)