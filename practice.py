import test_module

#Title method - makes first letter of each word uppercase
name = "ada lovelace"
print(name.title())

#Basic string concatenation
first_name = "Aaron"
last_name = "Austin"
full_name = first_name + " " + last_name
greeting = "Hello, " + full_name + "!"
print(greeting)

#Create newline and tab 
print("Python\n\tEasy\n\tFun\n\tEfficient")

#Remove whitespace using rstrip()
#rstrip() removes whitespace from end. lstrip() removes whitespace from front
#strip() removes whitespace from both
word = "hello "
word = word.rstrip()
print(word)

#Use Str() to convert a number to a string
age = 27
name = "aaron"
message = name + str(age) + " years old"
print(message)

#Operators
num1 = 4+4
num2 = 10-2
num3 = 4*2
num4 = 16/2
print(str(num1) + "\n" + str(num2) + "\n" + str(num3) + "\n" + str(num4))

#list
family_members = []
family_members.append("Aarionte")
family_members.append("Piggie")
family_members.append("Mom")
family_members.append("Tiare")
print(family_members)
family_members.insert(3, "Chaz")
print(family_members)
popped = family_members.pop(3)
family_members.remove("Tiare")
print(family_members)
print("Removed: " + popped + " and Tiare but they are still family!")
family_members = family_members.sort()
print(family_members)

letters = ["a","c","d","b"]
letters.sort()
print(letters)
letters.reverse()
print(letters)

#Basic For Loop
foods = ["fries", "turkey", "ham"]

for food in foods:
    print(food)

#Numerical For Loop
products = []

for value in range(1,11):
    products.append(value*2)
print(products)

products = [value*2 for value in range(10,21)]
print(products)

#For Loop to print odd numbers
num = []

for value in range(1,11,2):
    print(value)

#Slice - work with a specific group of data in a list
#Copy one list to another by slicing it. This points both list variables to the same list. Changes to one affect both - line 83
#Use slices to iterate through specific groups of data in a loop also - line 91
players = ["aaron", "ryan", "jake", "josh", "cody"]
new_players = players[:]
print(players)
print(new_players)
print(players[1:3])
print(players[:3])
print(players[4])
print(players[3:])
print(players[-3:])
for player in players[1:3]:
    print(player)

#Tuple - An immutable list (list that cannot change)
dimensions = (50, 40)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

#Dictionaries - A collection of key/value pairing(s)
person = {
    "name": "Aaron", 
    "age": 27,
    }
print(person["name"])
print(person["age"])

#Add a key/value pair to the dictionart
person["weight"] = 240
print(person["weight"])

#Modify a key/pair in a dictionary
person["name"] = "Austin"
print(person["name"])

#Remove key/value pair
del person["weight"]
print(person)

#Starting with an empty dictionary
cars = {}
cars["kia"] = "Kia Forte"
cars["ford"] = "Ford Explorer"
cars["dodge"] = "Dodge Charger"
print(cars)

#Iterate through keys and values in dictionary
for key, value in cars.items():
    print("\nKey " + key)
    print("Value " + value)

#Iterate through the keys in dictionary
for key in cars.keys():
    print("Key " + key)

#Iterate through the values of dictionary
for value in cars.values():
    print("Value " + value)

#Nesting dictionaries - a dictionary inside a list
bmw = {
    "color": "green",
    "miles": 20,
}
kia = {
    "color": "red",
    "miles": 50000,
}
ford = {
    "color": "blue",
    "miles": 3000,
}

cars = [bmw, kia, ford]
print(cars)

#Nesting dictionaries - list inside a dictonary
pizza = {
    "crust": "regular",
    "toppings": ["mushrooms", "sausage"],
}

print("You ordered a pizza with " + pizza["crust"] + " crust and the following toppings:")
for topping in pizza["toppings"]:
    print("\t" + topping)

#Multiple values to one key in a dictionary
foods = {
    "grilled": ["hamburger", "hotdog"],
    "fried": ["fish", "fries"],
}

for k, v in foods.items():
    print(k)
    print(v)

#A dictionry in a dictionary
users = {
    "aaron": {
        "first": "aaron",
        "last": "austin",
        "age": 27,

    },
    "tiare": {
        "first": "tiare",
        "last": "peters",
        "age": 24,
    },

}

def speak():
    """Print Hello"""
    print("I will count to 10")

def count():
    """Count to 10"""
    count = 0
    for value in range(10):
        count += 1
        print(count)

#Function with a standard parameter (number1) & a default value parameter(number2)
def add_three(number1, number2=2):
    sum = number1 + 3
    sum2 = number2 + 3
    print(sum)
    print(sum2)

def odd_even(number):
    if number % 2 == 0:
        print("Even")  
    else:
        print("Odd")

#Function with a default/optional parameter
def full_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    
    return full_name

#Function with an arbitrary amount of arguments
def test_func(*numbers):
    for value in range(len(numbers)):
        x = numbers[value] + 2
        print("Number " + str(value) + ": " + str(x))

def prac_func(first, last, **info):
    li = {}
    li["first"] = first
    li["last"] = last

    print(li["first"])
    print(li["last"])

    for k, v in info.items():
        li[k] = v
        print("Key: " + k, end=", ")
        print("Value: " + v + "\n")

#speak()
#count()

#The two add_three() methods belowdo the same things, the first just uses a positional call and the second uses a keyword call
#add_three(5,8)
#add_three(number1=5, number2=8)

#odd_even(5)
#print(full_name("Aaron", "Austin"))
#print(full_name("Jim", "Jones", "Jax"))
#test_func(3)
#test_func(5, 9, 6, 4)
#prac_func("Aaron", "Austin", age="21", height="72", weight="240")

#Function uses a function from test_module file (import)
test_module.add(10, 5)

#Github test change