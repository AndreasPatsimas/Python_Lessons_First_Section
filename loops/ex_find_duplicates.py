my_list = ["a", "b", "c", "b", "d", "e", "e"]

dupilcates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in dupilcates:
        dupilcates.append(item)

print(dupilcates)