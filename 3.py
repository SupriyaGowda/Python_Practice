age = input("Enter your age: ")  # Taking input from the user
print("Your age is:", age)  # Output: Your age is: (whatever the user entered)

Boy_name = input("Enter Boy name: ") # Taking input for name
Boy_age = int (input("Enter your age: ")) # Taking input for age
Girl_name = input("Enter Girl name: ") # Taking input for name
Girl_age = int (input("Enter your age: ")) # Taking input for age
age = abs(Boy_age - Girl_age)  # Calculating the age difference with absolute value to ensure it's positive

print(Boy_name + " loves " + Girl_name  + " " + str(age) )  # Output Concating the strings and age together using (+)

print(f"{Boy_name} loves {Girl_name} and their age difference is {age}")  # Output using f-string to format the output with variablesm