"""
The final module in Intermediate section is Testing and Debugging.
In this module, we will learn about various testing and debugging techniques in Python.
Testing and debugging are essential skills for any developer, as they help to ensure that our code is working correctly and efficiently.
We will cover different types of testing, including unit testing, integration testing, and functional testing.
We will also learn about debugging techniques, such as using print statements, logging, and using debugging tools like pdb.
By the end of this module, you will have a solid understanding of testing and debugging in Python, and you will be able to apply these techniques to your own projects.
------------------------------Unit Testing------------------------------
Unit testing is a type of testing that focuses on testing individual units or components of a program.
The goal of unit testing is to ensure that each unit of the program is working correctly and producing the expected output.
In Python, we can use the built-in unittest module to create and run unit tests.
Here's an example of how to create a simple unit test:
"""
import unittest
def add(a, b):
    return a + b
class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
if __name__ == '__main__':
    unittest.main()
# You see in above code we defined a simple function add that takes two parameters and returns their sum.
# We then created a unit test class TestMathUtils that inherits from unittest.TestCase.
# Inside the class, we defined a test method test_add that tests the add function using various inputs and expected outputs.
# Finally, we called unittest.main() to run the unit tests.

"""
------------------------------Debugging with pdb------------------------------
pdb is the built-in Python debugger that allows us to step through our code, set breakpoints, and inspect variables.
Here's an example of how to use pdb to debug a simple function:
"""
def divide(a, b):
    return a / b    
import pdb
pdb.set_trace()
result = divide(10, 0)
print(result)
# You see in above code we defined a simple function divide that takes two parameters and returns their division.
# We then imported the pdb module and called pdb.set_trace() to set a breakpoint.
# When we run the code, the execution will stop at the breakpoint, and we can use pdb commands to step through the code, inspect variables, and identify the error (in this case, division by zero).

"""
------------------------------Summary------------------------------
In this module, we learned about testing and debugging techniques in Python.
We covered unit testing using the unittest module and debugging using the pdb module.
These techniques are essential for ensuring that our code is working correctly and efficiently.
Make sure to practice these techniques by creating your own unit tests and using pdb to debug your code.
"""

"""------------------------------Practice time!------------------------------
1. Create a unit test for a function that calculates the factorial of a number.
2. Use pdb to debug a function that raises an exception when dividing by zero.
3. Create a unit test for a function that checks if a string is a palindrome.
4. Use pdb to step through a function that calculates the Fibonacci sequence.
5. Create a unit test for a function that sorts a list of numbers in ascending order.
"""