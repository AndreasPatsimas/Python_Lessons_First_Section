# for item in "I love volunteering":
#     print(item)

my_list = ["dockers", "kafka", "kubernetes"]

for item in my_list:
    if not(item.startswith("d")):
        print(item)

for i in range(0, len(my_list)):
    print(my_list[i])

my_dictionary = {
    "user":"andreas3",
    "password":"aris1914",
    "team":"Aris"
}

for item in my_dictionary.items():
    key, value = item
    print(key, value)

for i, item in enumerate(my_list):  # with this have the indexes
    print(i, item)

for i, item in enumerate(my_dictionary.items()):
    k, v = item
    print(i, k, v)