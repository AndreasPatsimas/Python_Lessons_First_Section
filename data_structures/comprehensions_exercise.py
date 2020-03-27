my_list = ["a", "b", "c", "b", "d", "e", "e"]

duplicates = list(set([char for char in my_list
              if my_list.count(char) > 1]))

# for item in my_list:
#     if my_list.count(item) > 1 and item not in dupilcates:
#         dupilcates.append(item)

print(duplicates)

