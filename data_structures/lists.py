shop_list = ["apple", "banana"]

shop_list.append("watermelon")

print(shop_list)

print("watermelon" in shop_list)

sentence = " "

new_sentence = sentence.join(["Hello", "volunteers", "I'm", "Andreas"])

print(new_sentence)

new_shop_list = ", ".join(shop_list)

print(new_shop_list)

# list unpacking
a,b,c = shop_list
print(a)