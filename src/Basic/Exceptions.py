# Handling exceptions properly is what separates a fragile script from a robust script.

"""
What is an Exception?
 - Exception is an event, errors or problems that happens when a program is running.
 - You can think like: Python raising it's hand and saying "Hey! Something went wrong and I don't know what to do!"
 - If you don't handle exceptions, your program will crash.
 for example: If you try to run int("Hello"), python will crash and this is a built-in exception called ValueError.
"""

"""
--------------- Try and Except Blocks ----------------
To handle exception in python, we use a try ... except block, It't like telling Python:
 - try : I want you try to run this risky piece of code.
 - except: If you fail, except for that, don't crash. Run this safety code instead.
syntax:
"""

try:
    # Risky code goes here
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except:
    # Safety code goes here
    # This block ONLY run if an error happens in the try block
    print("That's not a valid age! Please enter a number.")
print("Program continues...")

"""
explanation:
1. The code inside the try block is executed first.
2. If everything goes well, the except block is skipped.
3. If a ValueError occurs (like if the user enters "hello" instead of a number), the code inside the except block runs instead of crashing the program.
4. After handling the exception, the program continues running normally.
"""

"""
--------------- Catching Specific Exceptions ----------------
It's a good practice to catch specific exceptions rather than a generic except. This way, you can handle different errors differently.
for example:   
"""
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
explanation:
1. The try block contains code that might raise exceptions.
2. If a ValueError occurs (like entering non-numeric input), the first except block runs.
3. If a ZeroDivisionError occurs (like trying to divide by zero), the second except block runs.
4. This way, you can provide specific feedback based on the type of error.
"""

"""
--------------- Finally Block ----------------
Sometimes, you have code that must run no matter what, whether an exception occurred or not. You can use a finally block for this.
syntax:
    try:
        # Risky code
    except SomeException:
        # Handle exception
    finally:
        # This code runs no matter what
for example:
"""
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("Execution completed.")
    # Note: In real code, you should also close the file if it was opened successfully.
    # Here, for simplicity, we are not handling that.

"""
------------ else Block (Optional) --------------
You can also use an else block after all the except blocks. The code inside the else block runs only if no exceptions were raised in the try block.
syntax:
    try:
        # Risky code
    except SomeException:
        # Handle exception
    else:
        # This code runs if no exceptions occurred
for example:
"""

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print(f"You entered the number: {num}")
finally:
    print("End of program.")

"""
explanation:
1. The try block attempts to open and read a file.
2. If the file doesn't exist, a FileNotFoundError is raised, and the except block runs.
3. Regardless of whether an exception occurred or not, the finally block runs, ensuring that "Execution completed." is printed.
"""


"""
------------------ Summary --------------------
 - Exceptions are errors that occur during program execution.
 - Use try and except blocks to handle exceptions and prevent your program from crashing.
 - Catch specific exceptions to provide tailored error handling.
 - Use a finally block for code that must run regardless of whether an exception occurred.
"""

"""
------------------- Practice time--------------------
1. Write a program that asks the user to enter two numbers and divides them. Handle exceptions for invalid input and division by zero.
2. Create a function that reads a file and prints its content. Handle the exception if the file does not exist.
3. Modify the above function to include a finally block that prints "Finished attempting to read the file."
"""


