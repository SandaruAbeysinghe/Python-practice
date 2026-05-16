name = input("Input your name: ")
age = int(input("Input your age: "))
hundred = 2026 - age

if age >= 0 and age <120:
    print(name, "you will turn 100 in", hundred + 100)
else:
    print("Invalid input")
    
