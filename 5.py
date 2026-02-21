# Lists in Python

items = ['apple', 'banana', 'cherry']   # This is a list of strings
print(items)  # Output: ['apple', 'banana', 'cherry'] 
print(items[0])  # Output: 'apple' (accessing the first item)
print(items[-1])  # Output: 'cherry' (accessing the last item) 

items.pop()  # This will remove the last item from the list
print(items)  # Output: ['apple', 'banana'] (after popping the last item)

items.pop(0)  # Remove the item at index 0 (the first item)
print(items)  # Output: ['banana'] (after popping the first item)

items.append('orange')  # This will add 'orange' to the end of the list
print(items)  # Output: ['banana', 'orange']

items.append('grape')  # This will add 'grape' to the end of the list

items.remove("orange")  # Remove 'orange' from the list
print(items)  # Output: ['banana', 'grape'] (after removing 'orange')

items.insert(1, 'bisciut')  # This will insert 'bisciut' at index 1 (the second position in the list)
print(items)  # Output: ['banana', 'bisciut', 'grape'] (after inserting 'bisciut' at index 1) 

items.clear()  # This will remove all items from the list
print(items)  # Output: [] (after clearing the list)

items = ['apple', 'banana', 'cherry']  # Recreate the list
print(items)  # Output: ['apple', 'banana', 'cherry'] (the original list is back)

items[1] = 'blueberry'  # This will change the item at index 1 to 'blueberry'
print(items)  # Output: ['apple', 'blueberry', 'cherry'] (after changing 'banana' to 'blueberry')


numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)

print(len(items))  # Output: 3 (the number of items in the list)
print(len(numbers))  # Output: 7 (the number of items in the list)  

print(sorted(items))  # Output: ['apple', 'blueberry', 'cherry'] (sorted list  without changing the original list)

print(list(reversed(items)))  # Output: ['cherry', 'blueberry', 'apple'] (reversed list without changing the original list)

# Nested lists (lists within lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] (the nested list representing a matrix)

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)
print(matrix[2][2])  # Output: 7 (element in the third row, third column)