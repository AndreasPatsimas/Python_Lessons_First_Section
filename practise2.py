name = "Andreas"
age = 55

print(f"{name} is {age} old")

#or

print("{} is {} old".format(name, age))

print("{new_name} is {age} old".format(new_name = "Sotiris", age = 51))

print(name[0])

print(name[0:4])
#[start:stop:stepover]
print(name[0:4:2])

print(name[1:])
print(name[:2])
print(name[::2])

print(len(name)) # len = length

print(name.upper())

print(name.replace("nd", "fg"))