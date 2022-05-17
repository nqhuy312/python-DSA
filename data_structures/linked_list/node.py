

# =============================================================================


class Node:

    def __init__(self, data, pointer=None):
        self.__data = data
        self.__pointer = pointer

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
    def pointer(self, node):
        self.__pointer = node
        
    def __repr__(self):
        return (f"<Node {self.__data}, {self.__pointer}>")

    __str__ = __repr__

# =============================================================================

if __name__ == "__main__":
    head = Node(1)
    first = Node(2)
    second = Node(3)

    head.pointer = first
    first.pointer = second

    print(head)

