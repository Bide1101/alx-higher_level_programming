Python - Data Structures: Lists, Tuples
Python provides several built-in data structures for efficient and convenient data manipulation. Two of the most commonly used data structures in Python are Lists and Tuples.

Lists
Lists are mutable, ordered sequences of elements enclosed in square brackets ([]). The elements of a list can be of any data type, including other lists. The elements can be accessed using their index, which starts from 0 for the first element. Lists also support several built-in functions, such as len() to get the number of elements in a list, append() to add an element to the end of a list, and pop() to remove an element from the end of a list.

Here is an example of creating and manipulating a list:

# create a list of integers
my_list = [1, 2, 3, 4, 5]

# access an element of the list
print(my_list[0])  # 1

# change an element of the list
my_list[0] = 0
print(my_list)  # [0, 2, 3, 4, 5]

# add an element to the end of the list
my_list.append(6)
print(my_list)  # [0, 2, 3, 4, 5, 6]

# remove the last element of the list
my_list.pop()
print(my_list)  # [0, 2, 3, 4, 5]
Tuples
Tuples are immutable, ordered sequences of elements enclosed in parentheses (()). The elements of a tuple can be of any data type, including other tuples. The elements can be accessed using their index, which starts from 0 for the first element. Tuples also support several built-in functions, such as len() to get the number of elements in a tuple.

Here is an example of creating and manipulating a tuple:

# create a tuple of strings
my_tuple = ('apple', 'banana', 'cherry')

# access an element of the tuple
print(my_tuple[0])  # 'apple'

# try to change an element of the tuple (this will raise an error)
my_tuple[0] = 'orange'

# get the number of elements in the tuple
print(len(my_tuple))  # 3
Conclusion
In Python, lists and tuples are powerful data structures that can be used to store and manipulate data efficiently. While lists are mutable and support more operations, tuples are immutable and can be used when we want to make sure that the data remains unchanged. By understanding the differences between lists and tuples, you can choose the right data structure for your needs and write more efficient and effective code.
