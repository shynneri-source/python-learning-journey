# Loops 

# Loops let you run a block of code over and over again, Python has two main types of loops: for loops and while loops.

"""
1. For Loops
 - A for loop is used for interating over a sequence. A sequence is just an odered collection of items, like a list of name or a range of numbers.
 - Think of is as: "for each item in this collection, do this."
"""

"""
 ------------------Iterating over a sequence.--------------------
Let's introduce a new data type real quick. Because it's the most common thing to loop over: the list.
A list is just a collection of items inside square brackets [], separated by commas.
"""

names = ["shyn", "nova", "brige"]

for i in names:
    print(f"Hello, {i}!")
# In this example, the loop goes through each name in the names list and prints a greeting
'''
output: 
 -Hello, shyn!
 -Hello, nova!
 -Hello, brige!
'''

"""
------------------------- How it works -------------------------
1. python sees the for keyword and knows a loop is starting.
2. It take the first item from the names list ("shyn") and assigns it to the variable i.
3. It runs the indented block of code (the print statement), which uses i to print "Hello, shyn!".
4. Then it goes back to the for line, takes the next item from the list ("nova"), assigns it to i, and runs the print statement again
5. This continues until all items in the list have been processed.
"""

"""
------------------ Using range() --------------------
The most common way to use a for loop is to just repeat action x number of times. For this, we use the built-in range() function.
The range() function generates a sequence of numbers, which is perfect for looping a specific number of times.
for example:
"""

for numbers in range(5):
    print(f"This will print 5 times. Current number is: {numbers}")
# In this example, range(5) generates the numbers 0 through 4, and the loop runs 5 times.
'''
output:
This will print 5 times. Current number is: 0
This will print 5 times. Current number is: 1
This will print 5 times. Current number is: 2
This will print 5 times. Current number is: 3
This will print 5 times. Current number is: 4
'''

"""
Note: if you want to count from 1 to 10, you'd write range(1,11) because the end value is exclusive.
"""
for num in range(1, 11):
    print(num)

"""
------------------ While Loops --------------------
A while loop repeatedly runs a block of code as long as a certain condition is true.
Think of is as: "While this condition is true, keep doing this."
Syntax: while condition:
for example:
"""

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # This is shorthand for count = count + 1
print("loop finished.")
# In this example, the loop will keep running as long as count is less than 5

"""
Best practice: avoid infinite loops.
An infinite loop happens when the condition never becomes false, causing the loop to run forever. 
Always make sure something inside the loop will eventually make the condition false.
for example, in the above code, we increment count by 1 each time, so eventually count will reach 5 and the loop will stop.
"""

"""
------------------ controlling loop with break and continue --------------------
Sometimes, you need to change the loop behavior based on certain conditions.
 - Break: Stops the loop immediately. It just jumps out of the loop and continues with the code after the loop.
 - Continue: Skips the rest of the current loop iteration and jumps to the next iteration.
For example:
"""

for number in range(10):
    if number == 5:
        print("Number 5 found, breaking the loop.")
        break  # Exit the loop when number is 5
    if number % 2 == 0:
        print(f"{number} is even, skipping to next iteration.")
        continue  # Skip even numbers
    print(f"Processing number: {number}")


""" 
------------- Practice Time -------------
1. Write a for loop that prints all the numbers from 1 to 20.
2. Write a while loop that counts down from 10 to 1 and then prints "Liftoff!".
3. Write a for loop that goes through a list of your favorite fruits and prints each one.
4. Write a while loop that keeps asking the user for input until they type "exit".
"""