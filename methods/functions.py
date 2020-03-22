def say_hello():
    print("hello volunteers")

def see_emo(name, emo):
    print("Hello {}. Your emo is {}".format(name, emo))



say_hello()

#positional arguments
see_emo("Andreas", ':)')

#keywords arguments
see_emo(emo = ":(", name = "Konnina")

def sum(x, y):
    return x + y

result = sum(5, -2)

print(result)


