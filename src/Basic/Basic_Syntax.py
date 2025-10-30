# Basic Python Syntax

# Comments

"""
First things you must know is comments. A comment is a line of text in your code that Python will completely ignore. We use them to leave notes for ourselves or for other developers to explain what our code is doing.
In Python, any line that starts with a pound sign (#) is a comment.
But if you want have a multiple line comment like this comment you can use similar this comment
"""

# This is a comment and python don't run this line

'''
bla bla
This is a comment too
bla bla 
'''

"""
bla bla 
This also a comment
bla bla
"""

# Variables and Basic Data Types

"""
Think of a variable as a labeled box where you can store a piece of data. You give the box a name (the variable name) and put something inside it (the value).
Creating a variable is simple. You just use the equals sign (=).
"""

# Here, 'message' is the variable name, and "Hello, Wellcome to Shyn's python teaching repo!" is the value.
message = "Hello, Wellcome to Shyn's python teaching repo!" #so you can see this is a variable contain a string value

"""
Python figures out the type of data automatically. Let's look at the most common types:
 - String (str): Plain text. You create strings by wrapping your text in either double (") or single (') quotes.
 - Integer (int): Whole numbers, with no decimal point.
 - Float (float): Numbers with a decimal point.
"""

# A String (str)
my_name = "Shyn"

# An Integer (int)
my_age = 19

# A Float (float)
pi = 3.14159


# Printing Output

# To see the value of a variable or just print some text to the console, we use the built-in print() function.

print("Hello there!") # Prints the string directly

# You can also print the value stored in a variable
current_user = "shynneri" # You can change this line and see which difference in console
print(current_user)

"""
A very common and useful way to print is by using f-strings. These let you easily embed your variables directly inside a string. 
Just put an f before the opening quote and wrap your variable names in curly braces ({}).
"""

name = "Shyn" # Change this line if you want
print(f"hello, {name}")

age = 19
print(f"My english name is {name}, and currently i am {age} years old.")


"""
--------------- The Golden Rule: Indentation Matters! -----------------

This is the most important concept in Python syntax.
In many other languages, programmers use curly braces ({}) to define blocks of code (like what's inside a loop or a function). Python does not use braces.
Instead, Python uses indentation (the whitespace at the beginning of a line).
You don't need to worry about it for the simple variables we're writing now, but as soon as we get to functions, loops, or if statements, this becomes critical.
------ The Rule: Code that is part of the same block must be indented at the same level (usually by 4 spaces).
"""

# Here's a quick preview (don't worry about the if syntax, just look at the spacing):

weather = "sunny" # This code is not indented, it's at the "top level"

if weather == "sunny":
    # This line is indented (by 4 spaces)
    # it "belongs" to the "if" statements above it 
    print("Don't forget your sunglasses!")

print("Have a great day!") # This line is not indented, so it's outside the 'if' block and it will always run.

# If you mess up the indentation, your program will crash. It's how Python reads the "shape" of your logic.


# Practice Time

# So, we learned a lot of new things in the first lesson. You can slow down, do some practice, and improve everything you learned.

# This is some practice i built for you 

"""
P1: Variables: Create three variables:
   - favorite_song (a string)
   - lucky_number (an integer)
   - temperature (a float, like 98.6 or 20.5) Then, use the print() function to print each variable on its own line.
P2: What's the Output? Look at the code below. Without running it, what do you think it will print to the console? Just guess and remember before u write and run this code.
--------------------------------------------------------------------------------------------------------------------
item = "laptop"
cost = 1200
print(f"The {item} costs ${cost}.")
--------------------------------------------------------------------------------------------------------------------
Your Turn: Write a small program that creates a variable for your city and another for the current_year. Then, use an f-string to print a single sentence, like: "I am living in [City] in the year [Year]."
"""
