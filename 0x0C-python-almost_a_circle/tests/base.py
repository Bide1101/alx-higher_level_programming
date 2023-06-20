#!/usr/bin/python3
"""This is the base file"""
import json
import csv
import turtle


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_of_dictionaries):
        """This returns the JSON string representation of the given input"""
        if list_of_dictionaries is None or list_of_dictionaries == []:
            return "[]"
        return json.dumps(list_of_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A Class method that writes the JSON string representation
        of a given list to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """A method that returns the list represented in JSON format"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This creates an instance based on the given dict"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """This returns a list of instances"""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as json_file:
                list_dict = Base.from_json_string(json_file.read())
                return [cls.create(**obj) for obj in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This Writes a list of objects to a file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            w = csv.w(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    w.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    w.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """This loads a list of objects from a file"""
        objects = []
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                else:
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                obj = cls.create(**dic)
                objects.append(obj)
            return objects
