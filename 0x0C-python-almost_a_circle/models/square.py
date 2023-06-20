#!/usr/bin/python3
"""Python Almost a Circle - Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class (Square) inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor for the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """This Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """A string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """This updates the attributes of the Square"""
        if args and len(args) != 0:
            attr_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This returns the dictionary representation of Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
