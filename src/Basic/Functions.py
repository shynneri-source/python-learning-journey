
"""
--------------------What is a function?----------------------
A function is a reusable, named of block code that performs a specific task
Think of it like a recipe. A recipe has:
 - A name (e.g "recipe for pancakes")
 - A list of ingredients (input)
 - A set of instructions (the logic , process)
 - A final dish (output)
Functions help break down complex problems into smaller, manageable pieces. They also promote code reusability and organization.
"""

"""
built-in functions:
Python comes with many built-in functions that you can use right away, such as:
 - print(): Outputs text to the console.
 - len(): Returns the length of a string, list, or other collection.
 - int(): Converts a value to an integer.
 - str(): Converts a value to a string.
 - input(): Gets user input from the console.
You can use these functions without needing to define them yourself.
for example:
"""
name = input("Enter your name: ")  # Using the built-in input() function
print("Hello, " + name + "!")        # Using the built-in print() function
length = len(name)                   # Using the built-in len() function
print("Your name has " + str(length) + " characters.")  # Using str()

"""
--------------------Defining Your Own Functions----------------------
You can define your own functions using the def keyword, followed by the function name and parentheses.
syntax:
def function_name(parameters):
    # function body
    return output
for example:
"""

def greet_user(username):
    """This function greets the user by their name."""
    print("Hello, " + username + "! Welcome aboard.")

greet_user("shyn")  # Calling the function with "shyn" as an argument

"""
---------------Function Parameters and Arguments----------------------
Functions can take inputs called parameters. When you call a function, you provide arguments that correspond to those parameters.
for example:
"""

def add_numbers(a, b):
    """This function adds two numbers."""
    return a + b

result = add_numbers(5, 10)  # Calling the function with 5 and 10 as arguments
print("The sum is: " + str(result))

"""
---------------Return Statement----------------------
Functions can return values using the return statement. This allows you to get results back from the function
for example:
"""

def multiply_numbers(x, y):
    """This function multiplies two numbers and returns the result."""
    return x * y

product = multiply_numbers(4, 6)  # Calling the function and storing the returned value
print("The product is: " + str(product))

"""
---------------Exception Handling in Functions----------------------
You can handle exceptions within functions using try and except blocks to make your functions more robust.
for example:
"""

def divide_numbers(num1, num2):
    """This function divides two numbers and handles division by zero."""
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: You cannot divide by zero."
division_result = divide_numbers(10, 0)  # Calling the function with a zero divisor
print(division_result)


"""---------------Function Documentation----------------------
You can add documentation to your functions using docstrings. This helps others (and yourself) understand what the function does.
for example:
"""
def subtract_numbers(a, b):
    """This function subtracts the second number from the first number."""
    return a - b
print(subtract_numbers.__doc__)  # Accessing the docstring of the function

"""
---------------Lambda Functions----------------------
Lambda functions are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression.
syntax:
lambda parameters: expression
for example:
"""
square = lambda x: x * x  # Defining a lambda function to square a number
print("The square of 5 is: " + str(square(5)))  # Calling the lambda function

"""
---------------Function Scope----------------------
Variables defined inside a function are local to that function and cannot be accessed from outside. This is known as function scope.
for example:
"""
def my_function():
    local_variable = "I am local to this function." 
    print(local_variable)
my_function()
# print(local_variable)  # This would raise an error because local_variable is not accessible here

"""
---------------Recursion----------------------
A function can call itself, which is known as recursion. This is useful for problems that can be broken down into smaller, similar subproblems.
for example:
"""
def factorial(n):
    """This function returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("The factorial of 5 is: " + str(factorial(5)))


"""---------------Function Annotations----------------------
Function annotations allow you to add metadata about the types of parameters and return values.
syntax:
def function_name(param1: type1, param2: type2) -> return_type:
for example:
"""
def add_numbers(a: int, b: int) -> int:
    """This function adds two numbers."""
    return a + b    

print("The sum is: " + str(add_numbers(3, 7)))

"""
----------------Practice time!----------------------
1. Define a function that takes a list of numbers and returns the average.
2. Create a function that checks if a string is a palindrome (reads the same forwards and backwards).
3. Write a recursive function to compute the nth Fibonacci number.
4. Define a lambda function that takes two arguments and returns their maximum.
5. Write a function that takes a dictionary and returns a list of its keys sorted alphabetically
"""