#like maps -> key pair-value

shop_list = ["apple", "banana"]

my_dictionary = {
    "yo" : "men",
    "volun" : "teers",
    "shop" : shop_list,
    "really" : True
}

print(my_dictionary)

print(my_dictionary.get("yo"))
print(my_dictionary["yo"])

my_second_dictionary = {
    "yo" : "mana",
    "volun" : "teers",
    "shop" : shop_list,
    "really" : False
}

my_list = [my_dictionary, my_second_dictionary]

print(my_list)

#dictionaries keys must be immutable. as a result cannot be a list for a key, also key has to be unique

print("yo" in my_second_dictionary.keys())
print(shop_list in my_second_dictionary.values())
print(my_dictionary.items())

my_second_dictionary.update({"yo":"patera"})
print(my_second_dictionary)