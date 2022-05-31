from dequenode import DequeNode



# =============================================================================

class Deque:
    """Deque in linked list"""

    def __init__(self, data):
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
                tail = curr_node
                size += 1

        return head, tail, size

    def append(self, data):
        """ Append new node to linked list
        Args:
            node (Node) : Node to apppend

        Returns:
            (LinkedList) : return self to support cascade methods

        """

        node = DequeNode(data)

        if self.__tail:
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
            (LinkedList) : return self to support cascade methods

        """

        node = DequeNode(data)

        node.pointer = self.__head
        if not self.__head:
            self.__tail = node

        self.__head = node
        self.__len += 1

        return self

    def pop():
        pass

    def popleft():
        pass

    def __len__(self):
        return self.__len

    def __repr__(self):
        return(f"deque([{self.__head.__repr__()})]")

    __str__ = __repr__


# =============================================================================


if __name__ == "__main__":
    deque = Deque([])
    deque.append('word !!')
    deque.appendleft('hello')
    print(deque)