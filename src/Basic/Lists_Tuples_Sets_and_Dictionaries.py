"""
-------------------------Python 4 core collections-------------------------
Python has four built-in collection data types:
1. Lists
2. Tuples
3. Sets
4. Dictionaries
Each collection type has its own characteristics and use cases.
-----------------------------------------------------------------------------
Think of these as different ways to group and organize data in your programs.
This is a cheat sheet to help you understand and use these collections effectively.
------------------------------1. Lists--------------------------------------
Lists are ordered, mutable (changeable), and allow duplicate elements.
You can create a list using square brackets [].
for example:
[1, 2, 3]
------------------------------2. Tuples-------------------------------------
Tuples are ordered, immutable (unchangeable), and allow duplicate elements.
You can create a tuple using parentheses ().
for example:
(1, 2, 3)
------------------------------3. Sets---------------------------------------
Sets are unordered, mutable (changeable), and do not allow duplicate elements.
You can create a set using curly braces {} or the set() function.
for example:
{1, 2, 3}
------------------------------4. Dictionaries-------------------------------
Dictionaries are unordered, mutable (changeable), and store data in key-value pairs.
You can create a dictionary using curly braces {} with key-value pairs.
for example:
{"name": "Shyn", "age": 19}
------------------------------------------------------------------------------
----------------------------use cases of each collection----------------------
- Lists: Use lists when you need an ordered collection of items that may change over time, such as a list of tasks or a collection of user inputs.
- Tuples: Use tuples when you need an ordered collection of items that should not change, such as coordinates or fixed configuration settings.
- Sets: Use sets when you need a collection of unique items and want to perform operations like union, intersection, or difference, such as a collection of unique tags or categories.
- Dictionaries: Use dictionaries when you need to associate values with unique keys, such as user IDs or product codes.
"""

mylist = [1, 2, 3, 4, 5]  # Example of a list
mytuple = (1, 2, 3, 4, 5)  # Example of a tuple
myset = {1, 2, 3, 4, 5}    # Example of a set
mydict = {"name": "Shyn", "age": 19}  # Example of a dictionary

"""
You can perform various operations on these collections, such as adding, removing, and accessing elements.
Refer to the Python documentation for more details on how to work with each collection type.
But for example, here are some basic operations:
# List operations
mylist.append(6)  # Adding an element to the end of the list
print(mylist[0])  # Accessing the first element of the list
# Tuple operations
print(mytuple[1])  # Accessing the second element of the tuple
# Set operations
myset.add(6)  # Adding an element to the set
# Dictionary operations
print(mydict["name"])  # Accessing the value associated with the key "name"
print("Age is: " + str(mydict["age"]))  # Accessing the value associated with the key "age"

"""

"""
----------------Practice time!----------------------
1. Create a list of your favorite fruits and print the second fruit in the list.
2. Create a tuple containing the first five prime numbers and print the entire tuple.
3. Create a set of unique colors you like and add a new color to the set.
4. Create a dictionary with your name, age, and city, then print your age from the dictionary.
5. Write a function that takes a list of numbers and returns their sum.
6. Write a function that takes a dictionary and returns a list of its keys.
7. Write a function that takes a set and returns its length.
"""

"""
This is important knowledge for working with python! So make sure to practice and understand these concepts well.
You must master these to become proficient in Python programming.
Remember, practice makes perfect! Don't just read about these concepts, try to implement them in your own code.
"""