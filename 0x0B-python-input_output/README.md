Python - Input/Output

Introduction
Input/Output (I/O) operations are essential in any programming language as they allow interaction with the user and enable data storage and retrieval. In Python, there are various ways to handle input and output, including reading from the standard input, writing to the standard output, and performing file input/output operations.

This repository aims to provide examples and explanations of different I/O techniques in Python, helping you understand and leverage these capabilities effectively.

Reading Input
Python offers several methods to read input from the user. The most common approach is to use the input() function, which prompts the user for input and returns the entered value as a string.

name = input("Enter your name: ")
print("Hello, " + name)
In this example, the input() function is used to prompt the user to enter their name. The entered value is stored in the name variable and then displayed using the print() function.

It's important to note that the input() function always returns a string. If you need to read a different data type, such as an integer or a float, you can use type conversion methods like int() or float().

age = int(input("Enter your age: "))
print("You are", age, "years old.")
In this case, the input() function is used to read the age as a string. The value is then converted to an integer using the int() function and stored in the age variable. Finally, the age is printed using the print() function.

Writing Output
Python provides various ways to output data to the user. The most common method is to use the print() function, which displays the specified message or variable value.

name = "Alice"
print("Hello, " + name)
In this example, the print() function is used to display the message "Hello, Alice" on the screen. The + operator is used to concatenate the string literal with the value of the name variable.

You can also print multiple values or variables separated by commas.

age = 25
print("Name:", name, "Age:", age)
In this case, the print() function displays the values of the name and age variables, separated by spaces. The output will be "Name: Alice Age: 25".

File Input/Output
Python allows reading and writing data to files. To perform file I/O operations, you need to open the file using the open() function, which returns a file object. The file can be opened in different modes, such as read mode ('r'), write mode ('w'), or append mode ('a').

# Writing to a file
file = open("output.txt", "w")
file.write("Hello, world!")
file.close()
In this example, the open() function is used to open a file named "output.txt" in write mode. The write() method is then used to write the string "Hello, world!" to the file. Finally, the close() method is called to close the file and ensure data is saved.

# Reading from a file
file = open("input.txt", "r")
content = file.read()
file.close()
print(content)
In this case, the open() function opens a file named "input.txt" in read mode. The read() method reads the entire contents of the file, which are stored in the content variable. The file is then closed, and the content is printed using the print() function.

Formatting Output
Python provides various ways to format output using placeholders and formatting options. One commonly used method is the format() method, which allows you to insert values into a string at specific positions.

name = "Bob"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
In this example, curly braces {} are used as placeholders. The format() method replaces the placeholders with the values of the name and age variables, respectively. The resulting string is then printed.

Python also supports f-strings (formatted string literals) introduced in Python 3.6. F-strings provide a concise and convenient way to embed expressions inside string literals.

name = "Bob"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
In this case, the f prefix indicates that the string is an f-string. The expressions within curly braces {} are evaluated and replaced with their values during runtime.

Conclusion
Python provides powerful and flexible input/output capabilities. This repository has covered various aspects of input/output operations, including reading input from the user, writing output to the screen, performing file input/output, and formatting output. Understanding these concepts will allow you to create more interactive and versatile Python programs
