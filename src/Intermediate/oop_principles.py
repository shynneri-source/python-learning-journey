"""
This is next level after understanding the basic concepts of OOP.
We will learn about principles of OOP in this module.
Principles of OOP help us to design and structure our code in a better way.
They provide guidelines for creating classes and objects that are easy to understand, maintain, and extend.
We will cover the four main principles of OOP: Encapsulation, Abstraction, Inheritance, and Polymorphism.
------------------------------Encapsulation------------------------------
Encapsulation is the principle of bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class.
It restricts direct access to some of the object's components, which can prevent the accidental modification of data.
In Python, we can achieve encapsulation by using private attributes and methods.
Private attributes and methods are defined by prefixing their names with double underscores (__).
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):   # Public method to access private attribute
        return self.__name

    def set_age(self, age):  # Public method to modify private attribute
        if age > 0:
            self.__age = age

    def get_age(self):   # Public method to access private attribute
        return self.__age

person = Person("Shyn", 19)
print(person.get_name())  # Output: Shyn
person.set_age(20)
print(person.get_age())   # Output: 20
# You see in above code we defined a class Person with private attributes __name and __age.
# We provided public methods get_name, set_age, and get_age to access and modify these private attributes.
# This way, we encapsulated the data and provided controlled access to it.

"""
------------------------------Abstraction------------------------------
Abstraction is the principle of hiding the complex implementation details and showing only the essential features of the object.
It helps to reduce complexity and increase efficiency by allowing the user to focus on the high-level functionality rather than the low-level implementation.
In Python, we can achieve abstraction by using abstract classes and methods.
An abstract class is a class that cannot be instantiated and is meant to be subclassed.
An abstract method is a method that is declared but contains no implementation.
"""

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow"  
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof
print(cat.sound())  # Output: Meow
# You see in above code we defined an abstract class Animal with an abstract method sound.
# We created two subclasses Dog and Cat that implemented the sound method.
# This way, we provided a high-level abstraction of the Animal class while hiding the implementation details of the sound method.

"""
------------------------------Polymorphism------------------------------
Polymorphism is the principle that allows objects of different classes to be treated as objects of a common superclass.
It allows methods to do different things based on the object it is acting upon, even though they share the same name.
In Python, we can achieve polymorphism through method overriding and operator overloading.
"""

class Bird:
    def sound(self):
        return "Chirp"
class Fish:
    def sound(self):
        return "Blub"
def make_sound(animal):
    print(animal.sound())
bird = Bird()
fish = Fish()
make_sound(bird)  # Output: Chirp
make_sound(fish)  # Output: Blub
# You see in above code we defined two classes Bird and Fish with a method sound.
# We created a function make_sound that takes an animal object and calls its sound method.
# This way, we demonstrated polymorphism by allowing different objects (Bird and Fish) to be treated as objects of a common interface (having a sound method).

"""
This time to the most important part of OOP principles: Inheritance
Inheritance is the principle that allows a class (child class) to inherit attributes and methods from another class (parent class).
It promotes code reusability and establishes a hierarchical relationship between classes.
In Python, we can achieve inheritance by defining a child class that specifies the parent class in parentheses.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Inherit attributes from Vehicle
        self.doors = doors

    def honk(self):
        return "Beep beep"
my_car = Car("Toyota", "Corolla", 4)
print(my_car.start_engine())  # Output: Engine started
print(my_car.honk())          # Output: Beep beep
# You see in above code we defined a parent class Vehicle with attributes brand and model, and a method start_engine.
# We created a child class Car that inherited from Vehicle and added an additional attribute doors and a method honk.
# This way, we demonstrated inheritance by reusing the code from the Vehicle class in the Car class.

"""
-----------------------------Practice time!----------------------
1. Create a class named "Employee" with private attributes "name" and "salary".
   Add public methods to get and set these attributes.
2. Create an abstract class named "Shape" with an abstract method "area".
   Create two subclasses "Circle" and "Rectangle" that implement the "area" method.
3. Create a function that takes a list of different shape objects and prints their areas using polymorphism.
4. Create a parent class named "Person" with attributes "name" and "age".
   Create a child class named "Student" that inherits from "Person" and adds an attribute "student_id".
   Add a method to display the student's information. 
5. Create a child class named "Teacher" that inherits from "Person" and adds an attribute "subject".
   Add a method to display the teacher's information.
"""