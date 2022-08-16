username = input("username")
password = input("password")

encrypt_password = "*" * len(password)

print("Hey {}, your password {} length is {} letters long.".format(username, encrypt_password, len(password)))
