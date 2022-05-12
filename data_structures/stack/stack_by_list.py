"""
Stack by List
=============

Implement Stack data structure in Python by built-in list

Supported operations:
    * push(element): Add an element to the top of Stack
    * top(): Return top element of Stack
    * pop(): Remove and return top element of Stack
    * clear(): Remove all element of Stack
    * is_empty(): Check Stack is empty or not
    * len: Return length of Stack
"""

__author__ = "Huy Nguyen"
__email__ = "nqhuy312@gmail.com"
__date__ = "2022/05/12"
__status__ = "development"


# =============================================================================


import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


# =============================================================================


class ListStack:
    """List Stack Class"""

    def __init__(self, elements=None):
        """Stack Initialization

        Args:
            elements (list[object]): list of element to build stack
                (default: None)
        """

        self.__stack = ListStack.build_stack(elements)
    
    @staticmethod
    def build_stack(elements=None):
        """Build Stack with given input
        
        Args:
            elements (list[object]): list of element to build stack
                (default: None)
        
        Returns:
            (list): Stack with given input
        """

        return elements if isinstance(elements, list) else []
    
    def push(self, element):
        """Push an element to Stack

        Args:
            element (object): element need to push to Stack

        Returns:
            (Stack): itself
        """

        self.__stack.append(element)
        return self
    
    def top(self):
        """Get the top element of Stack
        
        Returns:
            (object): top element    
        """

        if self.__stack:
            return self.__stack[-1]
        raise ValueError
    
    def pop(self):
        """Pop the top element of Stack and return that element
        
        Returns:
            (object): top element
        """

        if self.__stack:
            return self.__stack.pop()
        raise ValueError 
    
    def clear(self):
        """Remove all elements from Stack"""

        self.__stack.clear()
    
    def is_empty(self):
        """Check Stack is empty or not
        
        Returns:
            (bool): Stack is empty or not
        """

        return len(self.__stack) == 0

    def __len__(self):
        """Get length of Stack
        
        Returns:
            (int): Length of Stack
        """

        return len(self.__stack)

    def serialize(self):
        """Get list of elements of Stack in serialization
        
        Returns:
            (list): list all elements of Stack    
        """

        return self.__stack[::-1][:]

    def __repr__(self):
        """Representation of Stack

        Returns:
            (str) : representaion of Stack
        """

        return repr(self.__stack)

    def __call__(self):
        """Caller function of Stack
        
        Returns:
            (list): Get list of elements of Stack in serialization
        """

        return self.serialize()


# =============================================================================


if __name__ == "__main__":
    logging.info('Task: Python List Stack\n')

    st = ListStack()
    assert len(st) == 0

    st = ListStack([1,2,3])
    st.push(4).push(5)
    print(st.top())
    assert len(st) == 5

    print(st)

    logging.info('Process Done!')
