name = input("What is your name? ")
print("Hello",  name)
age = input("How old are you? ")
#another way to format print is via f-strings
try:
    print(f"{name}, you were born in {2024 - int(age)}")
    division = int(age) / 0
except ZeroDivisionError: #if you run the code you can see the type of error
    print("Age must be a valid numeric value")
    print(f"the value that you typed was {age}")
except: #all other types of exceptions
    print("Something else went wrong")
print("thanks for playing")
