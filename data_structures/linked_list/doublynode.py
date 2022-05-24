"""
Linked List Doubly Node class
=================

Example on how to use Python built-in Linked List datatype
    * Construct Linked List Doubly Node Class
    * Representation
"""


__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2022/05/21'
__status__ = 'development'


# =============================================================================


class DoublyNode:
    """Linked List Doubly Node"""

    def __init__(self, data, pointer=None, previous=None):
        self.__data = data
        self.__pointer = pointer
        self.__previous = previous

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def pointer(self):
        return self.__pointer

    @pointer.setter
    def pointer(self, Node):
        self.__pointer = Node

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, Node):
        self.__previous = Node

    def __repr__(self):
        #return (f"{self.__previous} <- Node, {self.__data} -> {self.__pointer}")
        return (f" <- Node, {self.__data} ->")

    __str__ = __repr__

# =============================================================================


