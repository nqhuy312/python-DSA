"""
Doubly Linked List class
========================

Example on how to use Python built-in Linked List datatype
    * Construct an empty linked list (or from another linked list)
    * Append to linked list (from left/right/after and before a node)
    * Delete a node of linked list(from left/right/middle)
    * Representation


"""


__author__ = 'Khoa Tran'
__email__ = 'thdkhoa1312@gmail.com'
__date__ = '2022/05/21'
__status__ = 'development'


# =============================================================================


from doublynode import DoublyNode
import logging
import functools


# =============================================================================


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def DEBUG(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("="*79)
        func(*args, **kwargs)
        print('='*79)
    return wrapper


# =============================================================================


class DoublyLinkedList:
    """Linked List Class"""

    def __init__(self, *data):
        self.__head, self.__tail, self.__len = self.build_list(data)

    @property
    def head(self):
        return self.__head

    @staticmethod
    def build_list(data):
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
            head = tail = DoublyNode(data[0])
            size = 1

            for val in data[1:]:
                curr_node = DoublyNode(val)
                tail.pointer = curr_node
                curr_node.previous = tail
                tail = curr_node
                size += 1

        return head, tail, size

    def add_front(self, node):
        """ Append new node to the left doubly linked list
        Args:
            node (Node) : Node to apppend

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not isinstance(node, DoublyNode):
            return self

        node.pointer = self.__head

        if self.__head:
            self.__head.previous = node

        self.__head = node
        self.__len += 1

        return self

    def add_rear(self, node):
        """ Append new node to doubly linked list
        Args:
            node (Node) : Node to apppend

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not isinstance(node, DoublyNode):
            return self

        node.previous = self.__tail

        if self.__tail:
            self.__tail.pointer = node
        else:
            self.__head = node

        self.__tail = node
        self.__len += 1

        return self

    def add_after(self, prev_node, new_data):
        """ Append new node after the given node 
        Args:
            prev_node(Node): previous node of the new node
            new_data(int): data of the new node

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not isinstance(prev_node, DoublyNode):
            return self

        new_node = DoublyNode(new_data)

        new_node.pointer = prev_node.pointer
        new_node.previous = prev_node

        if prev_node.pointer is not None:
            prev_node.pointer.previous = new_node

        prev_node.pointer = new_node

        if prev_node == self.__tail:
            self.__tail = new_node

        self.__len += 1
        return self

    def add_before(self, after_node, new_data):
        """ Append new node before the given node 
        Args:
            after_node (Node) : after node of the new node
            new_data(int): data of the new node

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not isinstance(after_node, DoublyNode):
            return self

        new_node = DoublyNode(new_data)

        new_node.pointer = after_node
        new_node.previous = after_node.previous

        if after_node.previous is not None:
            after_node.previous.pointer = new_node

        after_node.previous = new_node

        if after_node == self.__head:
            self.__head = new_node

        self.__len += 1
        return self

    def pop_left(self):
        """ Delete the head node of linked list

        Returns:
            (LinkedList) : return self to support cascade methods

        """
        
        if self.__head:
            delete_node = self.__head

            if self.__head.pointer:
                self.__head.pointer.previous = self.__head.previous
            self.__head = self.__head.pointer

            if not self.__head:
                self.__tail = None
            
            del delete_node

            self.__len -= 1
        return self
    
    def pop(self):
        """ Delete the last node of linked list

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if self.__head:
            delete_node = self.__tail

            if self.__tail.previous:
                self.__tail.previous.pointer = self.__tail.pointer
            self.__tail = self.__tail.previous

            if not self.__tail:
                self.__head = None
            
            del delete_node

            self.__len -= 1
        return self

    def pop_middle(self):
        """ Delete the middle node of linked list

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if self.__head:
            middle = int(self.__len / 2)

            delete_node = self.__head
            for _ in range(middle):
                delete_node = delete_node.pointer

            delete_node.previous.pointer = delete_node.pointer

            if delete_node.pointer is not None:
                delete_node.pointer.previous = delete_node.previous
            
            del delete_node

            self.__len -= 1
        return self

    def __len__(self):
        return self.__len

    def __repr__(self):
        return(self.__head.__repr__())

    __str__ = __repr__


# =============================================================================


@DEBUG
def doubply_linkedlist_info(linked_list, message):

    if not isinstance(linked_list, DoublyLinkedList):
        raise Exception('Wrong type linked list')

    logging.info(message)
    length = len(linked_list)
    run_node = linked_list.head

    print(" "*79)
    print(f" {run_node.previous}", end='')
    for _ in range(length):
        print(run_node, end='')
        run_node = run_node.pointer

    print(f" {run_node}")
    print(" "*79)
    logging.info(f'Length of Linked List: {len(linked_list)}')


def test_doubly_linked_list():
    linked_list = DoublyLinkedList(7, 8, 9)
    doubply_linkedlist_info(linked_list, 'Start')

    four = DoublyNode(4)
    zero = DoublyNode(0)

    linked_list.add_rear(four)
    doubply_linkedlist_info(linked_list, 'Append 4')

    linked_list.add_front(zero)
    doubply_linkedlist_info(linked_list, 'Append Left 0')

    curr_node = linked_list.head
    for _ in range(len(linked_list)):
        if curr_node.data  == 4:
            linked_list.add_after(curr_node, 3)
            doubply_linkedlist_info(linked_list, 'Insert 3 after node 4')
        
        if curr_node.data == 8:
            linked_list.add_before(curr_node, 99)
            doubply_linkedlist_info(linked_list, 'Insert 99 before node 8')
        curr_node = curr_node.pointer

    linked_list.pop_left()
    doubply_linkedlist_info(linked_list, 'Pop left')

    linked_list.pop()
    doubply_linkedlist_info(linked_list, 'Pop')

    linked_list.pop_middle()
    doubply_linkedlist_info(linked_list, 'Pop middle')


# =============================================================================


def main():
    """Main process for testing
    """

    test_doubly_linked_list()


# =============================================================================

if __name__ == '__main__':
    logging.info('Task: Python Doubly Linked List\n')

    main()

    logging.info('Process Done!')
