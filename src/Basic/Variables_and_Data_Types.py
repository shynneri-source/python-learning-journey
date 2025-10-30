# Variables and Data Types

# What is a variable? (quick review)

# we said a variable is like a labeled box for storing data


my_age = 19 # 'my_age' is the label on the box and '19' is the value we put inside the box

# The 'label' (now we must call it is variable name) is how we find and use that data later

"""
----------------- Rule of naming Variables ------------------

Python has a few rules (and one strong convention) for naming:
 - Must start: Names must start with letter (a - z or A - Z) or an underscore (_).
 - Can contain: After the first character, name can contain letter, number (0 - 9) and underscore.
 - Nospace and special chars: You can't use space or characters like @, #, $, %, &, *, etc.
 - Case-sensitive: This is important! my_age is a different variable from My_age or MY_AGE.
"""

# Best practice (idiomatic python): we use "snake_case" for variable names. That just means all lowercase words connected by underscore

# Good variable names (snake_case)
first_name = "shyn"
user_is_logged_in = True
total_cost = 19.99

# Bad variable names (avoid these)
"""
first-name = "shyn" -- uses a dash, which is subtraction
1st_user = "hehe" -- starts with a number
total cost = 100 -- contain a space
"""

# What are data types?

"""
A data type is simply the category or kind of data you're storing.Python needs to know if it's working with text, whole numbers, or decimal numbers so it how to treat them.
for example, it know it can add 5 + 10 but it can't add "hello" + 5 in the same way.
Python is the dynamically typed. This sounds fancy, but it just mean you don't have to tell Python the type.
Python is smart enough to figure it out on its own when you assign the value.
"""

# String. A string is just plain text. You create one by wrapping text in single quotes (') or double quotes ("). It doesn't matter which you use, as long as you match them.
greeting = "hello"
response = 'hi there!'
user_name = "shyn"
quote = "He said, 'Python is awesome!'"

# Integer. An integer is a whole number (no decimal point).

item_count = 5
score = 100
name = "shyn"

# Float. A float is a number with a decimal point.
price = 19.99
temperature = 36.6
pi_value = 3.14

# Boolean. A boolean represents one of two values: True or False. (Note the capital T and F)
is_logged_in = True
has_paid = False
is_admin = False
is_equal = 5 == 6  # This will be False
is_greater = 10 > 3  # This will be True

# The nothing type: None. None is a special data type that represents the absence of a value. It's often used to indicate that a variable doesn't have any meaningful data yet.
winner = None
# It can be meaningful later in the program

if score == 100:
    winner = "Player 1"

# How to check a variable's data type?
# You can use the built-in type() function to check the data type of a variable.
print(type(greeting))  # Output: <class 'str'>
print(type(item_count))  # Output: <class 'int'>
print(type(price))  # Output: <class 'float'>
print(type(is_logged_in))  # Output: <class 'bool'>
print(type(winner))  # Output: <class 'NoneType'>


# Practice time 
"""
Let's test your knowledge with some practice!
1. Identify the Type: For each value below, identify its data type (string, integer, float, boolean, or None).
    - "100"
    - 100
    - False
    - 100.1
    - None
    
2. What's the output? Predict the output of the following code snippets:
    - item = "coffee mug"
    - quantity = 3
    - price_per_item = 12.99
    - in_stock = True
    - total_cost = quantity * price_per_item
    - print(type(item))
    - print(type(quantity))
    - print(type(price_per_item))
    - print(type(in_stock))
    - print(type(total_cost))
    
3. The intentional bug: What will be the result of the following code? Explain why.
    - num1 = "5"
    - num2 = 10
    - result = num1 + num2
    - print(result)
    - print(type(result))

"""