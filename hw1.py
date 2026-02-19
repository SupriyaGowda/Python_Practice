'''1. Simple Greeting Program: 
Write a Python program that asks the user for their name and age, 
then prints a personalized greeting message. Use both the + operator and f-strings for output.
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("welcome " + name + " and age is " + str(age))
print(f"welcome {name} and your age is {age}")

'''2.String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.'''

message = input("one line about you:  ")
print(message)
print(message.upper())
print(message.lower())
print(message.replace(" ", "_"))
print(message.strip())

'''3.Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.'''

message = input("prive the message: ")
print(len(message))