#tuple is an immutable list

my_tuple = ("ap", 2, True)

print(my_tuple)

#convert tuple to a list and universe

#1
my_list = list(my_tuple)
my_list.append("ap")
print(my_list)

#2
tlist = ["fd", 2]
ltuple = tuple(tlist)
print(ltuple)