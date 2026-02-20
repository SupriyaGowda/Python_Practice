# Logical Operator Practice: 

'''1.Write a Python program that takes two numbers as input from the user and checks if:
>Both numbers are greater than 10 (using and).
>At least one of the numbers is less than 5 (using or).
>The first number is not greater than the second (using not).'''

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print(a > 10 and b > 10)
print(a < 5 or b < 5)
print(not (a > b))

'''2.Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:
>"You are an adult" if the age is greater than or equal to 18.
>"You are a minor" if the age is less than 18.
>Use >= and < comparison operators.'''

age = int(input("Enter your age: "))
print(age)
print(age >= 18 and "You are an adult" or "You are a minor")

'''
3.Membership Operator Exercise: Write a Python program that:
>Takes a string as input from the user.
>Checks if the letter 'a' is in the string (using in).
>Checks if the string doesn't contain the word "Python" (using not in).
'''

message = input("one line about you")
print("world" in message)
print("python" not in message)


'''
4.Bitwise Operator Task: Given two integers, write a Python program that:
>Prints the result of a & b, a | b, and a ^ b.
>Shifts the bits of a two positions to the left (a << 2).
>Shifts the bits of b one position to the right (b >> 1).'''

a = 10  # In binary: 1010
b = 20  # In binary: 10100
print(a & b)  # Output: 0 because the bitwise AND of 1010 and 10100 is 00000.
print(a | b)  # Output: 30 because the bitwise OR of 1010 and 10100 is 11110.
print(a ^ b)  # Output: 30 because the bitwise XOR of 1010 and 10100 is 11110.  
print(a << 2)  # Output: 40 because shifting the bits of 1010 two positions to the left results in 101000, which is 40 in decimal.
print(b >> 1)  # Output: 10 because shifting the bits of 10100 one position to the right results in 1010, which is 10 in decimal.


