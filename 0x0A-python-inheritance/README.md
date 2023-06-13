Python Inheritance
In object-oriented programming, inheritance is a fundamental concept that allows classes to inherit attributes and methods from other classes. In Python, this powerful feature enables code reuse and promotes the organization and structure of programs.


Introduction to Inheritance
Inheritance allows us to define a new class, known as a subclass, that inherits attributes and methods from an existing class, known as a parent class or superclass. The subclass can then add or modify functionality without altering the parent class itself.

The key benefits of inheritance are:

Code Reusability: Inherited attributes and methods can be reused in multiple subclasses, reducing code duplication.
Modularity: Inheritance helps in organizing classes into a hierarchical structure, enhancing the program's structure and maintainability.
Polymorphism: Inheritance allows objects of a subclass to be treated as objects of the parent class, enabling polymorphic behavior.

Creating a Subclass
To create a subclass, we define a new class and specify the parent class in parentheses after the class name. This establishes an inheritance relationship between the parent class and the subclass.

class Subclass(ParentClass):
    # Subclass attributes and methods
    pass

Inheriting Attributes and Methods
When a subclass is created, it automatically inherits all attributes and methods from its parent class. This means that the subclass can access and use those attributes and methods without redefining them.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    pass

my_car = Car("Toyota")
print(my_car.brand)  # Inherited attribute from Vehicle class
my_car.start_engine()  # Inherited method from Vehicle class
Method Overriding
Subclasses have the ability to override methods inherited from the parent class. By redefining a method in the subclass, we can provide a new implementation that differs from the parent class.

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is moving")

my_car = Car()
my_car.move()  # Overrides the move method in Vehicle class
Accessing the Parent Class
Subclasses can access the attributes and methods of the parent class using the super() function. This allows the subclass to extend or modify the behavior of the parent class while still leveraging its functionality.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Accesses the parent class constructor
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.brand)  # Inherited attribute from Vehicle class

Multiple Inheritance
Python supports multiple inheritance, which allows a class to inherit from multiple parent classes. This enables a subclass to inherit attributes and methods from multiple sources, leading to diverse and flexible class hierarchies.

class ParentClass1:
    pass

class ParentClass2:
    pass

class Subclass(ParentClass1, ParentClass2):
    pass

Method Resolution Order (MRO)
In the case of multiple inheritance, Python follows a specific Method Resolution Order (MRO) to determine the order in which methods are resolved. The MRO is determined using the C3 linearization algorithm, and it ensures that methods are inherited in a consistent and predictable manner.

class ParentClass1:
    def do_something(self):
        print("ParentClass1 method")

class ParentClass2:
    def do_something(self):
        print("ParentClass2 method")

class Subclass(ParentClass1, ParentClass2):
    pass

my_object = Subclass()
my_object.do_something()

Abstract Base Classes
Python supports abstract base classes (ABC), which are classes that cannot be instantiated and serve as a blueprint for subclasses. ABCs define a common interface that subclasses must adhere to, ensuring a consistent structure and behavior.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

my_rectangle = Rectangle(5, 4)
print(my_rectangle.area())  # Implements the area method from Shape class

Conclusion
Inheritance is a powerful mechanism in Python that enables code reuse and facilitates object-oriented programming. It allows classes to inherit attributes and methods from parent classes, promotes code organization, and supports polymorphism. By understanding and utilizing inheritance effectively, you can write more efficient and maintainable code.
