name = input("What is your name? ")
print("Hello",  name)
age = input("How old are you? ")
try:
    print(f"{name}, you were born in {2024 - int(age)}")
except ZeroDivisionError: #if you run the code you can see the type of error
    print("Age must be a valid numeric value")
    print(f"the value that you typed was {age}")
except: #all other types of exceptions
    print("Something else went wrong")
else: #in case no exception happened
    print("Thanks for being a good sport and not trying to crash the app")
finally: #this runs in the end no matter what
    print("thanks for playing")