"""
-----------------------Decorators-------------------------
A decorator is a special type of function that modifies the behavior of another function.
Decorators allow you to wrap a function with another function, enabling you to add functionality before and after the original function is called, without modifying its code.
In Python, decorators are defined using the "@" symbol followed by the decorator function name above the target function.
Think of it like a wrapper:
    - You have a gift (the original function).
    - You wrap it with decorative paper (the decorator).
    - When someone opens the gift, they see the decoration first (the added functionality) before getting to the gift itself (the original function).
Decorators can be used for various purposes, such as logging, authentication, and input validation.
For example:
"""

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before calling the original function.")
        result = original_function(*args, **kwargs)
        print("After calling the original function.")
        return result
    return wrapper_function
@decorator_function
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Shyn")
# You see in above code we defined a decorator function decorator_function that adds behavior before and after calling the original function say_hello.
# When we call say_hello("Shyn"), it first prints "Before calling the original function.", then calls the original function to print "Hello, Shyn!", and finally prints "After calling the original function.".         

"""
The @ syntax is just a shorthand for applying the decorator to the function.
It means:
say_hello = decorator_function(say_hello)
This way, the say_hello function is now wrapped with the behavior defined in the decorator_function
""" 

"""
-----------------------Context Managers-------------------------
A context manager is a special type of construct in Python that allows you to set up a temporary context for a block of code to run in.
It is commonly used for resource management, such as opening and closing files, managing database connections, or acquiring and releasing locks.
The most common way to use a context manager is with the "with" statement.
When you use a context manager with the "with" statement, it automatically handles the setup and teardown of the context for you.
For example:
"""
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# You see in above code we used the with statement to open a file named "example.txt" in write mode.
# The context manager takes care of opening the file and ensures that it is properly closed after the block of code is executed, even if an error occurs within the block.
# This way, we don't have to worry about closing the file manually, which helps prevent resource leaks and makes the code cleaner and more readable.

"""
---------------------------How Context Managers Work-------------------------
When you use a context manager with the "with" statement, it follows these steps:
1. The context manager's __enter__() method is called, which sets up the context (e.g., opening a file).
2. The block of code inside the "with" statement is executed.
3. After the block of code is executed, the context manager's __exit__() method is called, which tears down the context (e.g., closing the file).
This ensures that resources are properly managed and cleaned up, even if an error occurs within the block of code.
"""

"""
------------------------------Practice time!----------------------
1. Create a decorator that logs the execution time of a function.
2. Create a context manager that measures the time taken to execute a block of code.
3. Use a decorator to check if a user is authenticated before allowing access to a function.
4. Create a context manager that temporarily changes the current working directory.
5. Write a decorator that retries a function call if it raises an exception, up to a specified number of attempts.
"""


