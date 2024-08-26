print("exercise 5")
#username = "python"
#password = "rules"
i = 0
user = input("Enter your username: ")
passw = input("Enter your password: ")

while user != "python" and passw != "rules":
    user = input("Enter your username: ")
    passw = input("Enter your password: ")
    i = i + 1
    if i == 4:
        print("Access denied!")
        break
else: print("Welcome")