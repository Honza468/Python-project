#This is a comment
#This code was written in VIM, in Graz (AT)
#17. 2. 2026

#These are basics of Python
print("Hello, world") #Only prints this to terminal
name = input("Enter your name: ")
print("Hello,", name," Welcome!")

location = input("Enter your current location: ")
age = input("Enter your age: ")

print("Your name is:", name)
print("You live in:", location)
print("Your age is:", age)

#---------------------------------------
x, y = input("Enter two values: ").split()
print("First number:", x)
print("Second number:", y)

namex, namey = input("Name your values here: ").split()
print(namex,"is",x)
print(namey,"is",y)

#---------------------------------------
name2, location2, age2 = input("Enter your name, location and age: ").split()
print("Welcome,",name2,"!" )
print("You are currently in:",location2)
print("You are now",age2,"years old!")

#---------------------------------------
name3 = input("Enter your name here: ")
print("You are welcomed here,",name3)
age3 = int(input("Enter your age here: "))
print("You are",age3,"old!")
weight = float(input("Please, enter your weight here: "))
print("You weigh",weight)
weight2 = input("Enter if in kilograms or pounds: ")
print("You weigh",weight,weight2)

#--------------------------------------
print(type(name))
print(type(age))
print(type(location))

print(type(x))
print(type(y))
print(type(namex))
print(type(namey))

print(type(name2))
print(type(location2))
print(type(age2))

print(type(name3))
print(type(age3))
print(type(weight))
print(type(weight2))

