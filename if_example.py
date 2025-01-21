#Import library with randomness
from random import choice

#Virtual Bartender
drinks = ["vodka", "wiskey", "gin", "tequila", "rum", "rakia", "sake"]
print("Welcome to the Virtual Pub")
name = input("I am the virtual batender, how do I call you? ")
try:
    age = input(f"How old are you, {name}? ")
    age = int(age) #convert to a number
    if age >= 21:
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f" Based on you age I need to ask where you are from, {name}?")
        legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and country != "USA":
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
    if age > 120 or age < 5:
        print(f"Please do not lie to the virtual bartender!")
    elif legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
        print(f"Dear {name}, I cannot serve you")
except ValueError:
    print("Please give a valid age")