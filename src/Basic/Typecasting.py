# What is Typecasting?

"""
Typecasting (or type conversion) is the process of explicitly telling python to change a value from one data type to another.
why would we do this? The most common reason is that we get data format like a string but we need it in another like an integer to do work.
Think of it like this: you have "5" and 10 , so you want to add them together. 
But the "5" is a string, and 10 is an integer. Python won't let you add them directly because they are different types.
So, you need to convert the "5" from a string to an integer first. This is where typecasting comes in.
Python is strongly-typed, which means it won't let you mix data types without explicit conversion. that's why typecasting is important.
"""

# Typecasting Functions
# int(): Converts a value to an integer.
# float(): Converts a value to a float (decimal number).
# str(): Converts a value to a string.

# Examples of Typecasting
# Converting string to integer
str_num = "5"
int_num = int(str_num)  # Now int_num is 5 (integer)
print(int_num + 10)  # Output: 15
# Without typecasting, this would raise an error:
# print(str_num + 10)  # This would cause a TypeError
# Converting string to float
str_float = "19.99"
float_num = float(str_float)  # Now float_num is 19.99 (float
print(float_num + 0.01)  # Output: 20.0
# Converting integer to string
age = 25
age_str = str(age)  # Now age_str is "25" (string)
print("I am " + age_str + " years old.")  # Output: I am
# Converting float to integer
price = 19.99
price_int = int(price)  # Now price_int is 19 (integer, decimal part is discarded)
print(price_int)  # Output: 19
# Note: when converting from float to integer, the decimal part is truncated (not rounded).
# be careful with typecasting, as it can lead to data loss (like truncating decimals) or errors if the conversion isn't valid (like converting "hello" to an integer).

"""
------------------ Summary --------------------
Typecasting is a crucial concept in Python that allows you to convert data from one type to another.
This is especially useful when dealing with user input or data from external sources, which often come in as strings.
By using typecasting functions like int(), float(), and str(), you can ensure that your data is in the correct format for your operations.
Always be mindful of the potential pitfalls, such as data loss or conversion errors, when typecasting.
"""

"""
------------------- Practice time--------------------
1. Convert the string "123" to an integer and add 10 to it. Print the result.
2. Convert the float 45.67 to an integer and print the result.
3. Convert the integer 100 to a string and concatenate it with " is a number".
4. What happens if you try to convert the string "hello" to an integer? Try it and observe the result.
"""