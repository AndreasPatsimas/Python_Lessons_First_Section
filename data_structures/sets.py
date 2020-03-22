# unordered collection of unique objects

my_set = {"da", 3, True, "da"}
my_set.add("sgdk")
my_set.add("da")
print(my_set)

my_list = [1,2,3,4,5,5]
print(my_list)
your_set = set(my_list)
print(your_set)
your_list = list(your_set)
print(your_list)

#useful methods
print(my_set.difference(your_set))
print(your_set.difference(my_set))

print(my_set)

#my_set.discard("da")
#print(my_set.intersection(your_set)) σημειο τομης
#print(my_set.union(your_set)) ενωση

print(my_set)
