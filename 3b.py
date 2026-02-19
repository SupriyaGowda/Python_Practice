First_name = "Krutansh"
Last_name = "Gowda"

print("My name is " + First_name + " " + Last_name) #concatenation
# Output: My name is Krutansh Gowda

print(f"{First_name} {Last_name}")


message = "warning! " * 5 #repetition
print(message) #repetition 
# Output: warning! warning! warning! warning! warning!

message = "warning! "
print(message * 5) #repetition
# Output: warning! warning! warning! warning! warning!

print(message.upper()) #string method
# Output: WARNING! 

print(message.lower()) #string method   

print(message.strip()*2) #string method to modified the string by removing any leading and trailing whitespace characters   
# Output: warning!warning!

print(message.replace("warning", "alert")) #string method to replace a specific substring with another substring    

name = "Krutansh said 'hello'" #Using single quotes inside a string that is enclosed in double quotes allows you to include the single quotes without needing to escape them. This is a common way to handle strings that contain quotes.

print(name)
# Output: Krutansh said 'hello'

name = 'Krutansh said "hello"' #Using double quotes inside a string that is enclosed in single quotes allows you to include the double quotes without needing to escape them. This is another common way to handle strings that contain quotes.
print(name)
# Output: Krutansh said "hello"

name = 'Krutansh said \'hello\'' #Using backslash to escape the single quotes allows you to include them in a string that is enclosed in single quotes. This is useful when you want to use the same type of quotes for the string and the content.
print(name)
# Output: Krutansh said 'hello'

name = '''Krutansh said 'hello'
        siri said "hi"
        priya said "love you both" ''' #Using triple quotes allows you to create multi-line strings and include both single and double quotes without needing to escape them. This is a convenient way to handle complex strings that contain various types of quotes and span multiple lines.
print(name)

print(len(message)) #string method to find the length of the string
# Output: 9

name = "Krutansh"
print(name[0]) #string indexing to access the first character of the string (position = index-1)
# Output: K
print(name[2:7]) #string indexing to access the second character of the string dispaly the characters from index 2 to index 6 (7-1)
# Output: utans
print(name[:5]) #string indexing to access the first five characters of the string (index 0 to index 4)
# Output: Kruta
print(name[3:]) #string indexing to access the characters from index 3 to the end of the string
# Output: tansh
print(name[-1]) #string indexing to access the last character of the string (negative indexing starts from the end of the string)
# Output: h     
print(name[-4:-1]) #string indexing to access the characters from index -4 to index -2 (negative indexing starts from the end of the string)
# Output: tans  
print(name[::2]) #string slicing to access every second character of the string
# Output: Kuta


name = "Krutansh is a \n good boy"
print(name) #The \n is an escape character that represents a newline, so it will create a line break in the output when printed.

print("Hello\tWorld") #The \t is an escape character that represents a tab, so it will create a horizontal space between "Hello" and "World" when printed.