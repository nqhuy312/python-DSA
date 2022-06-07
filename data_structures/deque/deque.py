"""
Deque Class
===========

Deque data structure

A double-ended queue. Element in Deque container can be added or removed element by both LIPO and PIPO machanism

Supported operations:
    * Constructor: 
        - Empty Deque
        - From list of integer numbers
    * append(val) : insert a number to the right of Deque
    * append_left(val) : insert a number to the left of Deque
    * pop() : remove the right most element of Deque
    * pop_left() : remove the left most element of Deque 
    * front() : return the left most element of Deque
    * rear() : return the right most element of Deque
    * clear() : clear all elements of Deque
    * is_empty() : whether Deque is empty of not
    * representation : show list of elements in Deque
"""


__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2022/05/30'
__status__ = 'development'


# =============================================================================


from dequenode import DequeNode
import logging


# =============================================================================


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# =============================================================================

class Deque:
    """Deque class by linked list"""

    def __init__(self, data=None):
        self.__head, self.__tail, self.__len = self.build_deque(data)

    @staticmethod
    def build_deque(data):
        """Create base Linked List
        Args:
            data (sequence) : sequence contains list of nodes

        Returns:
            head (Node): The head node of Linked List
            tail (Node): The tail node of Linked List
            len (int): The length of Linked List

        """

        head, tail, size = None, None, 0
        if data:
            head = tail = DequeNode(data[0])
            size = 1

            for val in data[1:]:
                curr_node = DequeNode(val)
                tail.pointer = curr_node
                curr_node.previous = tail
                tail = curr_node
                size += 1

        return head, tail, size

    def front(self):
        """Return most right element

        Returns:
            (int) : value of most right element
        """

        return self.__head

    def rear(self):
        """Return most right element

        Returns:
            (int) : value of most right element
        """

        return self.__tail

    def append(self, data):
        """ Append new node to linked list
        Args:
            node (Node) : Node to apppend

        Returns:
            (Deque) : return self to support cascade methods

        """

        node = DequeNode(data)

        node.previous = self.__tail

        if self.__tail:
            node.previous = self.__tail
            self.__tail.pointer = node
        else:
            self.__head = node

        self.__tail = node
        self.__len += 1

        return self

    def appendleft(self, data):
        """ Append new node to the left deque
        Args:
            data (Any) : Node to apppend

        Returns:
            (Deque) : return self to support cascade methods

        """

        node = DequeNode(data)

        node.pointer = self.__head

        if self.__head:
            node.pointer = self.__head
            self.__head.previous = node

        self.__head = node
        self.__len += 1

        return self

    def pop(self):
        """ Delete the last node of linked list

        Returns:
            (Deque) : return self to support cascade methods

        """
        if self.__head:
            delete_node = self.__tail
            self.__tail = self.__tail.previous
            self.__tail.pointer = None
            del delete_node

            self.__len -= 1
        return self

    def popleft(self):
        """ Delete the head node of linked list

        Returns:
            (Deque) : return self to support cascade methods

        """
        if self.__head:
            delete_node = self.__head
            self.__head = self.__head.pointer
            self.__head.previous = None
            
            del delete_node
            self.__len -= 1
        return self
    
    def clear(self):
        """Delete all element in deque. Return an empty Deque

        Returns:
            (Deque) : itself to support cascaded operations
        """

        self.__head = self.__tail = None
        self.__len = 0
        return self

    def is_empty(self):
        """Check if the deque is empty or not

        Returns:
            (bool) : the checking result
        """

        return False if self.__head else True


    def __len__(self):
        return self.__len

    def __repr__(self):
        return(f"deque([{self.__head.__repr__() if self.__head else ''}])")


    __str__ = __repr__


# =============================================================================


def test_len():
    """Test `len` function"""

    dq = Deque()

    assert len(dq) == 0

    lst = [-10]
    dq = Deque(lst)
    assert len(dq) == len(lst)

    lst = [1, 2, 9]
    dq = Deque(lst)
    assert len(dq) == len(lst)


# =============================================================================


def test_constructor():
    """Test deque constructor"""

    dq = Deque()
    assert repr(dq) == 'deque([])'

    lst = [-10]
    dq = Deque(lst)
    assert repr(dq) == 'deque([-10])'

    lst = [1, 2, 9]
    dq = Deque(lst)
    assert repr(dq) == 'deque([1, 2, 9])'


# =============================================================================


def test_clear():
    """Test clear method"""

    lst = [1, 2, 9]
    dq = Deque(lst)
    dq.clear()
    assert repr(dq) == 'deque([])'

    dq = Deque([])
    assert repr(dq) == 'deque([])'


# =============================================================================


def test_append():
    """Test append method"""

    dq = Deque()
    dq.append(1)

    assert repr(dq) == 'deque([1])'
    assert len(dq) == 1

    dq = Deque([4, 5, 6])
    lst = [7, 8, 9]

    for num in lst:
        dq.append(num)

    assert repr(dq) == 'deque([4, 5, 6, 7, 8, 9])'
    assert len(dq) == 6


# =============================================================================


def test_append_left():
    """Test append left method"""

    dq = Deque()
    dq.appendleft(10)

    assert repr(dq) == 'deque([10])'
    assert len(dq) == 1

    dq = Deque([4, 5, 6])
    lst = [7, 8, 9]

    for num in lst:
        dq.appendleft(num)

    assert repr(dq) == 'deque([9, 8, 7, 4, 5, 6])'
    assert len(dq) == 6


# =============================================================================


def test_pop():
    """Test pop method"""

    dq = Deque()
    dq.pop()

    assert repr(dq) == 'deque([])'

    dq = Deque([1, 2, 3, 4, 5, 6])
    for _ in range(3):
        dq.pop()
    
    assert repr(dq) == 'deque([1, 2, 3])'


# =============================================================================

def test_pop_left():
    """Test pop-left method"""

    dq = Deque()
    dq.pop()

    assert repr(dq) == 'deque([])'

    dq = Deque([1, 2, 3, 4, 5, 6])
    for _ in range(3):
        dq.pop()
    
    assert repr(dq) == 'deque([1, 2, 3])'


def test_combination():
    """Inspection test method"""

    dq = Deque([1, 2, 3])

    dq.pop()
    assert len(dq) == 2
    assert repr(dq) == 'deque([1, 2])'
    assert dq.is_empty() == False

    dq.append(4)
    assert repr(dq) == 'deque([1, 2, 4])'
    assert len(dq) == 3

    dq.popleft()
    dq.appendleft(10)

    assert repr(dq) == 'deque([10, 2, 4])'
    assert len(dq) == 3

    dq.clear()

    assert len(dq) == 0
    assert dq.is_empty() == True


# =============================================================================


def main():
    test_len()

    test_constructor()

    test_clear()

    test_append()

    test_append_left()

    test_pop()

    test_pop_left()

    test_combination()


# =============================================================================


if __name__ == "__main__":
    logging.info('Task: Python Deque\n')

    main()

    logging.info('Process Done!')

