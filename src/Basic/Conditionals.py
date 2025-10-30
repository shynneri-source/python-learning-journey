# Conditionals (if, elif, else)

"""
In life, we make decisions all the time. "If it's raining, we take an umbrella; if it's sunny, we wear sunglasses."
Conditionals are how we write that same logic in code. They allow your program to check a condition and then run a specific block of code only if that condition is true.
The condition is just any expression that evaluates to a boolean value (True or False).
"""

# The building block

"""
1. The 'if' statement (the if-then)
This is simplest conditional. It's the basic if-then check.
    -  if this condition is true
    -  then run the indented code block
    -  if the condition is false, the indented code block just skipped.
Syntax: notice the if , the condition, the colon :, and the indented block of code.
"""

age = 19
# The condition is age >= 18
if age >= 18:
    print("You are an adult.") # This line runs because the condition is true
print("This line runs no matter what.") # This line runs regardless of the condition
# It's not indented, so it's not part of the if block

# The 'else' statement (the or-else)
# This is the "otherwise" part of your umberella example. Else gives you a block of code to run only the condition is false.
if age < 18:
    print("You are not an adult.") # This line runs because the condition is true
else:
    print("You are an adult.") # This line runs if the condition is false

# In this example, since age is 19, the else block runs.

# The 'elif' statement (the else-if)
# This is for when you have multiple conditions to check in sequence.
# You can have as many elif blocks as you want between the if and else.
# for example, checking age groups:
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# Here, since age is 19, the second block runs.

"""
---------------- Tools for better conditionals ----------------
To build your conditionals, you can use comparison operators and logical operators.
Comparison Operators:
-  ==  (equal to)
-  !=  (not equal to)
-  <   (less than)
-  <=  (less than or equal to)
-  >   (greater than)
-  >=  (greater than or equal to)
Watch out: a very common mistake is using a single equals sign = (which is for assignment) instead of the double equals == (which is for comparison).
This error can appear in code of beginners so you must be careful.

Logical Operators:
-  and  (both conditions must be true)
-  or   (at least one condition must be true)
-  not  (negates the condition)
"""

# For example:
temperature = 75
if temperature > 60 and temperature < 80:
    print("The weather is nice.")
if temperature < 60 or temperature > 80:
    print("The weather is extreme.")
if not (temperature > 70):
    print("It's not warm.")
# In this case, only the first condition is true, so "The weather is nice." is printed.

# Nested Conditionals
# You can also nest conditionals inside other conditionals.
if age >= 15:
    if age < 18:
        print("You are a teenager but not old enough to drink in the VN.")
    else:
        print("You are an adult and old enough to drink in the VN.")
# Here, the outer if checks if the person is an adult, and then the inner if checks if they are old enough to drink.
# Since age is 19, the output will be "You are an adult but not old enough to drink in the VN."

# That's the basics of conditionals! They let your code make decisions and run different blocks of code based on different conditions.

"""
----------------- Practice time -----------------
1. Write a program that checks if a number is positive, negative, or zero.
2. Write a program that checks if a person is eligible to vote (age 18 or older).
3. Write a program that checks if a year is a leap year (divisible by 4, but not by 100 unless also divisible by 400).
"""

