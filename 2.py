student = {"name": "Supriya", "age": 20}    # Dictionary with keys "name" and "age"
is_student = False  # Boolean value no ""t a string
wieght = 55.5

print(student["name"], student["age"])  # Output: Supriya 20 
print(is_student)   # Output: false
print(type(wieght))  # Output: <class 'float'>
print(type(is_student))   # Output: <class 'bool'>

is_student = "yes"  # Updating the value of is_student
print(type(is_student))  # Output: <class 'str'>

s = "100"
print(int(s) + wieght) 

a = 10
b = 20
print(a + b)  # Output: 30


a = 20
b = 10
print(a-b)  # Output: 10
print(a*b)  # Output: 200
print(b/a)  # Output: 2.0  
print(a / b)  # Output: 0.5
print(a // b)  # Output: 2 (Floor Division)
print(a % b)   # Output: 0 (Modulus)
print(a ** b)  # Output: 10000000000 (Exponentiation)

print("befor swapping: a =", a, "b =", b)  # Output: before swapping: a = 20 b = 10
a, b = b, a  # Swapping the values of a and b
print("after swapping: a =", a, "b =", b)  # Output: after swapping: a = 10 b = 20


