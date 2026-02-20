a = 10
a = a + 100
print(a)

a+= 100 # a = a + 100 is the same as a += 100, it is a shorthand operator that adds the value on the right to the variable on the left and assigns the result back to the variable on the left.
print(a)

a*= 2 # a = a * 2 is the same as a *= 2, it is a shorthand operator that multiplies the variable on the left by the value on the right and assigns the result back to the variable on the left.
print(a)

a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= 10)  # Output: True
print(b <= 25)  # Output: True

print(10 > 5 and 5 < 3)  # Output: False because the first condition (10 > 5) is true but the second condition (5 < 3) is false, and for the 'and' operator to return true, both conditions must be true.
print(10 > 5 or 5 < 3)  # Output: True because the first condition (10 > 5) is true, and for the 'or' operator to return true, at least one of the conditions must be true.
print(not (10 > 5))  # Output: False because the condition (10 > 5) is true, and the 'not' operator negates it, making the overall expression false.    


string = "Welcome to Python programming!"
string2 = "Hello "
print("W" in string)  # Output: True because the substring "W" is present in the string "Welcome to Python programming!".

print(("world" in string) and "hello" in string2)  # Output: False because the substring "world" is not present in the string "Welcome to Python programming!", even though "hello" is present in "Hello ".

print("world" not in string)  # Output: True because the substring "world" is not present in the string "Welcome to Python programming!", and the 'not' operator negates it, making the overall expression true.