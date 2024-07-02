new_dict = {"name":"rajat","age":24,"skills":["python","gaming","music"]}
new_dict["phone"] = "8888-888888"
new_dict.update({"number of limbs":4, "age":24.4})
del new_dict["skills"]
new_dict.pop("age")

print(len(new_dict))
print(new_dict.keys())
print(new_dict.values())
print(new_dict["phone"])
print(new_dict.get("name"))
print(new_dict)