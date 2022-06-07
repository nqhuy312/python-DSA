"""
Deque Node Class
================

Implement linked list node for Deque
    * Construct doubly linked List node for Deque
    * Representation
"""


__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2022/05/30'
__status__ = 'development'


# =============================================================================


class DequeNode:
    """Linked List Doubly Node for Deque"""

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
        self.__comma = f', {self.__pointer}' if self.__pointer else ''
        return (f"{self.__data}{self.__comma}")

    __str__ = __repr__

