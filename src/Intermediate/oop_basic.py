"""
Object-Oriented Programming Basic Concepts
=======================================================
OOP is very important and useful in python and in this lesson, we will cover the basic concepts of OOP in python.
"""

"""
-----------------------------The class (the blueprint)-----------------------------
The class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
We use class many times in our code to create objects that share the same attributes and methods.
Class is very useful in organizing our code and making it more readable and maintainable.
"""

class Dog:
    # Attributes
    species = "Canis familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def bark(self):
        return f"{self.name} says woof!"

"""
You can see in above code we defined a class named Dog with attributes species, name, and age, and a method bark.
Don't worry if you don't understand everything right now, we will explain everything in detail in the following sections.
"""

"""
------------------------------The object (the instance)-----------------------------
The object is an instance of a class. It is created using the class blueprint and has its own unique attributes and methods.
We can create multiple objects from the same class, each with its own unique attributes and methods.
"""

bigbull = Dog("Big Bull", 5)
smallbull = Dog("Small Bull", 2)   
print(bigbull.bark())  # Output: Big Bull says woof!
print(smallbull.bark())  # Output: Small Bull says woof!

"""
You see in above code we created two objects bigbull and smallbull from the Dog class.
Each object has its own unique attributes (name and age) and can use the bark method defined in the Dog class.
"""

"""
----------------------------Initializer / Constructor----------------------------
The initializer (also known as constructor) is a special method in a class that is called when an object is created.
It is used to initialize the attributes of the object.
The initializer method is defined using the __init__() method.
"""

class Cat:
    def __init__(self, name, color): # This is the initializer method
        self.name = name # Initializing the name attribute
        self.color = color # Initializing the color attribute
    # So after creating an object of the Cat class, we can access the name and color attributes.


my_cat = Cat("Whiskers", "Tabby") # Creating an object of the Cat class
print(my_cat.name)  # Output: Whiskers
print(my_cat.color)  # Output: Tabby
# You see , we created an object my_cat of the Cat class and accessed its attributes name and color because we initialized them in the initializer method.
# If we didn't define the __init__() method, we wouldn't be able to set the name and color attributes when creating the object.
# But we have another way to initialize attributes without using the __init__() method but it's not recommended.

class Bird:
    species = "Aves"  # Class attribute
    name = ""  # Instance attribute
    color = ""  # Instance attribute

my_bird = Bird()  # Creating an object of the Bird class
my_bird.name = "Tweety"  # Setting the name attribute
my_bird.color = "Yellow"  # Setting the color attribute
print(my_bird.name)  # Output: Tweety
print(my_bird.color)  # Output: Yellow
# You see in above code we created an object my_bird of the Bird class and set its attributes name and color without using the __init__() method.
# But it's not recommended because it makes the code less readable and maintainable.
# So it's better to use the __init__() method to initialize the attributes of the object

"""
------------------------------Methods in a class------------------------------
Methods are functions that are defined inside a class and are used to perform operations on the objects of the class.
Methods can access and modify the attributes of the object and can also perform other operations.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

my_circle = Circle(5)
print(my_circle.area())  # Output: 78.5
print(my_circle.circumference())  # Output: 31.400000000000000002
# You see in above code we defined a class Circle with methods area and circumference.
# We created an object my_circle of the Circle class and called the area and circumference methods to calculate the area and circumference of the circle.

"""
------------------------------Self parameter------------------------------
The self parameter is a reference to the current instance of the class.
It is used to access the attributes and methods of the class in Python.
When defining methods in a class, the first parameter must always be self.
When calling a method on an object, we do not need to pass the self parameter explicitly, Python does it automatically.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

my_rectangle = Rectangle(4, 6)
print(my_rectangle.area())  # Output: 24
print(my_rectangle.perimeter())  # Output: 20
# You see in above code we defined a class Rectangle with methods area and perimeter.
# We created an object my_rectangle of the Rectangle class and called the area and perimeter methods to calculate the area and perimeter of the rectangle.
# The self parameter is used to access the width and height attributes of the object.  

"""
------------------------------Summary------------------------------
In this lesson, we covered the basic concepts of Object-Oriented Programming (OOP) in
Python, including classes, objects, initializers, methods, and the self parameter.
These concepts are fundamental to understanding OOP and will be used extensively in more advanced OOP topics.
Make sure to practice these concepts by creating your own classes and objects to reinforce your understanding.
We can learn about four principles of OOP: Encapsulation, Abstraction, Inheritance, and Polymorphism in next lessons but now.
"""
"""
----------------------------Practice time----------------------------
1. Create a class named "Car" with attributes "make", "model", and "year".
2. Add a method named "get_info" that returns a string containing the car's information.
3. Create an object of the "Car" class and call the "get_info" method to display the car's information.
4. Create a class named "Person" with attributes "name" and "age".
5. Add a method named "greet" that returns a greeting message using the person's name.
6. Create an object of the "Person" class and call the "greet" method to display the greeting message.
7. Create a class named "Square" with an attribute "side_length".
8. Add methods named "area" and "perimeter" that calculate and return the area and perimeter of the square.
9. Create an object of the "Square" class and call the "area" and "perimeter" methods to display the area and perimeter of the square.
10. Create a class named BankAccount with the following specifications:
Attributes:
 - owner (the name of the account owner)
 - balance (the amount of money in the account, default 0)
Methods:
 - deposit(amount) — adds money to the balance.
 - withdraw(amount) — subtracts money from the balance only if there is enough money, otherwise print "Insufficient funds".
 - get_balance() — returns the current balance.
Then:
 - Create an object of the BankAccount class.
 - Deposit some money, withdraw some money, and print the final balance.
"""