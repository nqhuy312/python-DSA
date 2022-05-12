from re import I
from node import Node

# =============================================================================


class LinkedList:

    def __init__(self, *data):
        self.__head, self.__tail, self.__len = self.build_list(data)
        print(self.__head, self.__tail)

    @staticmethod
    def build_list(data):
        head, tail, size = None, None, 0
        if not data:
            return head, tail, size

        head = tail = Node(data[0])
        size = 1

        for val in data[1:]:
            curr_node = Node(val)
            tail.pointer = curr_node
            tail = curr_node
            size += 1

        return head, tail, size

    def add_front(self, node):

        if not isinstance(node, Node):
            return self

        elif not self.__head:
            self.__head = node

        else:
            node.pointer = self.__head
            self.__head = node

        self.__len += 1
        return self

    def add(self, idx, node):
        if not isinstance(node, Node) or idx > self.__len:
            return self

        elif not self.__head:
            self.__head = node
        else:
            run_node = self.__head
            for i in range(self.__len):
                curr_node = run_node
                run_node = curr_node.pointer

                if idx == i:
                    curr_node.pointer = node
                    node.pointer = run_node

        self.__len += 1
        return self

    def add_rear(self, node):
        if not isinstance(node, Node):
            return self

        elif not self.__head:
            self.__head = node
        else:
            self.__tail.pointer = node
            self.__tail = node

        self.__len += 1
        return self

    def __len__(self):
        return self.__len

    def __repr__(self):
        return(self.__head.__repr__())

    __str__ = __repr__


# =============================================================================

if __name__ == "__main__":
    linked_list = LinkedList()

    four = Node(4)
    zero = Node(0)
    six = Node(6)
    linked_list.add_rear(four)
    linked_list.add_front(zero)
    linked_list.add(1, six)
    print(linked_list)
    print(len(linked_list))
