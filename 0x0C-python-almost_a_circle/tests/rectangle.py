#!/usr/bin/python3
"""A class called Rectangle that inherits from the Base class"""


from models.base import Base


class Rectangle(Base):
    """Represents a class (Rectangle) with its own attributes and the
    setters and getters for its attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor of the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property getter for the instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the attribute width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Property getter for the instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the attribute height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Property getter for the attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the attribute x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Property getter for the attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the attribute y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """This method returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """This method prints out the rectangle using '#' character"""
        print("\n" * self.__y, end='')
        for _ in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """This overrides the __str__ method to represent the Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """This method assigns arguments to each attribute"""
        if args and len(args) != 0:
            count = 0
            for argument in args:
                if count == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                elif count == 1:
                    self.width = argument
                elif count == 2:
                    self.height = argument
                elif count == 3:
                    self.x = argument
                elif count == 4:
                    self.y = argument
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """This method returns the dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
