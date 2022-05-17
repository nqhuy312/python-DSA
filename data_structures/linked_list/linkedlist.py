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
            self.__tail = node

        else:
            node.pointer = self.__head
            self.__head = node

        self.__len += 1
        return self

    def add(self, idx, node):
        if not isinstance(node, Node) or \
            not 0 <= idx <= self.__len - 1:
            return self

        elif not self.__head:
            self.__head = node
            self.__tail = node
        elif idx == 0:
            self.add_front(node)
        elif idx == self.__len:
            self.add_rear(node)
        else:
            prev_node = self.__head
            for i in range(1, self.__len):
                if idx == i:
                    node.pointer = prev_node.pointer
                    prev_node.pointer = node
                    break
                prev_node = prev_node.pointer

        self.__len += 1
        return self

    def delete(self, idx):
        if not 0 <= idx <= self.__len - 1:
            return self
        elif idx == 0:
            self.__head = self.__head.pointer

        else:
            prev_node = self.__head
            for i in range(1, self.__len):
                curr_node = prev_node.pointer
                if idx == i:
                    prev_node.pointer = curr_node.pointer
                
                self.__tail = prev_node
                prev_node = prev_node.pointer

        self.__len -= 1
        return self

    def add_rear(self, node):
        if not isinstance(node, Node):
            return self

        elif not self.__head:
            self.__head = node
            self.__tail = node
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
    linked_list = LinkedList(7,8,9)

    four = Node(4)
    zero = Node(0)
    six = Node(6)

    print(linked_list)
    print(len(linked_list))
    linked_list.add_rear(four)
    print(linked_list)
    print(len(linked_list))
    linked_list.add_front(zero)
    print(linked_list)
    print(len(linked_list))
    linked_list.add(1, six)
    print(linked_list)
    print(len(linked_list))
    linked_list.delete(5)
    print(linked_list)
    print(len(linked_list))
    # linked_list.delete_rear()
    # print(linked_list)
    # print(len(linked_list))
