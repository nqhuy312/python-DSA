"""
Doubly Linked List class
=================

Example on how to use Python built-in Linked List datatype
    * Construct an empty linked list (or from another linked list)
    * Append to linked list (from left/right/at given index)
    * Delete a node at given index
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
        print(self.__head, self.__tail)

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
        """ Append new node to linked list
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

    def add_after(self, node):
        """ Append new node by the given index
        Args:
            node (Node) : Node to apppend

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not isinstance(node, DoublyNode) or \
                not 0 <= idx < self.__len:
            return self

        if idx == 0:
            self.add_front(node)
        elif idx == self.__len - 1:
            self.add_rear(node)
        else:
            if self.__head:
                prev_node = self.__head
                for _ in range(idx-1):
                    prev_node = prev_node.pointer
                node.pointer = prev_node.pointer
                prev_node.pointer = node

            else:
                self.__head = node
                self.__tail = node

            self.__len += 1

        return self

    def delete(self, idx):
        """ Delete node at given index
        Args:
            idx (int) : the node index

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        if not 0 <= idx < self.__len:
            return self

        old_head = None
        if idx == 0:
            old_head = self.__head
            self.__head = self.__head.pointer
            del old_head
        else:
            prev_node = self.__head
            for i in range(1, self.__len):
                curr_node = prev_node.pointer
                if idx == i:
                    old_head = curr_node
                    prev_node.pointer = curr_node.pointer

                self.__tail = prev_node
                prev_node = prev_node.pointer

        del old_head
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
    logging.info('Doubply Linked List')
    length = len(linked_list)

    run_node = linked_list.head

    print(" "*79)
    for idx in range(length):
        # print(run_node.previous, run_node, run_node.pointer,  end="" if idx < length - 1 else '\n')
        print(run_node.previous, run_node, run_node.pointer)
        run_node = run_node.pointer

    print(" "*79)
    logging.info(f'Length of Linked List: {len(linked_list)}')


def test_doubly_linked_list():
    linked_list = DoublyLinkedList(7, 8, 9)

    four = DoublyNode(4)
    zero = DoublyNode(0)
    six = DoublyNode(6)
    eleven = DoublyNode(11)
    ten = DoublyNode(10)
    one = DoublyNode(1)
    two = DoublyNode(2)

    linked_list.add_rear(four)
    doubply_linkedlist_info(linked_list, 'Append 4')

    linked_list.add_front(zero)
    doubply_linkedlist_info(linked_list, 'Append Left 0')

    # linked_list.add(1, six)
    # linkedlist_info(linked_list,'Add idx 1 - 6')

    # linked_list.add(0, ten)
    # linkedlist_info(linked_list,'Add idx 0 - 10')

    # linked_list.add_rear(two)
    # linkedlist_info(linked_list,'Append 2')

    # linked_list.add(len(linked_list)-1, eleven)
    # linkedlist_info(linked_list,'Add idx len - 1 - 11')

    # linked_list.delete(5)
    # linkedlist_info(linked_list,'Delete index 5')

    # linked_list.add_rear(one) # linkedlist_info(linked_list,'Append 1')

# =============================================================================


def main():
    """Main process for testing
    """

    test_doubly_linked_list()


# =============================================================================

if __name__ == '__main__':
    logging.info('Task: Python Linked List\n')

    main()

    logging.info('Process Done!')
