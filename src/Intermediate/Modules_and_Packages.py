"""
So far we have learned about Python.
We have covered various topics including data types, control flow, functions, and more.
Now, We will dive into modules and packages in Python.
You can see modules and packages as a way to organize and structure your code.
--------------------------------Modules------------------------------
A module is a file containing Python code that defines functions, classes, and variables.
Modules help to organize code into manageable sections, making it easier to read, maintain, and reuse.
To use a module in your code, you can import it using the import statement.
For example, Python has a built-in module called math that provides various mathematical functions and constants.
You can use it like this:
"""

import math
result = math.sqrt(16)
print(result)  # Output: 4.0
# You see in above code we imported the math module and used its sqrt function to calculate the square root of 16.

"""
------------------------------building your own module------------------------------
You can create your own module by simply creating a Python file with a .py extension.
For example, let's create a module named my_module.py with the following content:
def greet(name):
    return f"Hello, {name}!"
Now, you can use this module in another Python file by importing it:
import my_module
message = my_module.greet("Shyn")
print(message)  # Output: Hello, Shyn!
You see in above code we created a module named my_module with a function greet.
We then imported this module in another file and used the greet function to generate a greeting message.
"""

"""
------------------------------Packages------------------------------
A package is a way to organize related modules into a directory hierarchy.In this lesson, You saw i im
A package is simply a directory that contains a special file named __init__.py and one or more module files.
The __init__.py file can be empty, but it indicates to Python that the directory should be treated as a package.
To use a package, you can import it using the import statement, similar to how you import modules.
For example, let's say we have a package named my_package with the following structure:
my_package/
    __init__.py
    module1.py
    module2.py
You can import and use the modules in the package like this:
import my_package.module1
import my_package.module2
Now, you can use the functions and classes defined in module1 and module2.
"""


"""
------------------------------Summary------------------------------
In this module, we learned about modules and packages in Python.
Modules help to organize code into manageable sections, while packages allow us to group related modules together.
By using modules and packages, we can create more organized, maintainable, and reusable code.
"""

"""
------------------------------Practice time!------------------------------
1. Create a module named "math_utils.py" that contains functions for basic mathematical operations (addition, subtraction, multiplication, division).
2. Create a package named "string_utils" that contains two modules: "case_utils.py" (for changing string cases) and "format_utils.py" (for formatting strings).
3. Use the functions from the "math_utils" module and the "string_utils" package in a separate Python file to perform various operations.  
"""

