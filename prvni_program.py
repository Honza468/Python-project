# This is a comment
# This code was written in VIM, in Graz (AT)
# 17. 2. 2026

# Code was updated in VIM, in Graz (AT)
# 19. 2. 2026
# All information about my work on this project is on Github


#These are basics of Python
print("Hello, world") #Only prints this to terminal
name = input("Enter your name: ")
print("Hello,", name," Welcome!")

location = input("Enter your current location: ")
age = input("Enter your age: ")

print("Your name is:", name)
print("You live in:", location)
print("Your age is:", age)

line = "-------------------------------------------------"

#---------------------------------------
print(line)

x, y = input("Enter two values: ").split()
print("First number:", x)
print("Second number:", y)

print(line)

namex, namey = input("Name your values here: ").split()
print(namex,"is",x)
print(namey,"is",y)

print(line)

#---------------------------------------
name2, location2, age2 = input("Enter your name, location and age: ").split()

print(line)

print("Welcome,",name2,"!" )
print("You are currently in:",location2)
print("You are now",age2,"years old!")

print(line)

#---------------------------------------
name3 = input("Enter your name here: ")
print("You are welcome here,",name3)

print(line)

age3 = int(input("Enter your age here: "))
print("You are",age3,"old!")

print(line)

weight = float(input("Please, enter your weight here: "))
print("You weigh",weight)
weight2 = input("Enter if in kilograms or pounds: ")
print("You weigh",weight,weight2)

print(line)

#--------------------------------------
print(type(name))
print(type(age))
print(type(location))

print(line)

print(type(x))
print(type(y))
print(type(namex))
print(type(namey))

print(line)

print(type(name2))
print(type(location2))
print(type(age2))

print(line)

print(type(name3))
print(type(age3))
print(type(weight))
print(type(weight2))

print(line)

#---------------------------------------
a, b, c, d = 1, 2, 3, 4 #Multiple assignments - assigning different values
z1 = z2 = z3 = 100 #Multiple assignments

print(a, b, c, d, z1, z2, z3) #printing out all the values

print(line)

#---------------------------------------
string = "10"
integrer = int(string)

integrer2 = 5
floatNumber = float(integrer2)

integrer3 = 25
string2 = str(integrer3)

print(integrer)
print(floatNumber)
print(string2)

print(line)
