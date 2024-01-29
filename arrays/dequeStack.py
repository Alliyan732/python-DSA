"""
Implementing stack using list disadvantages:
Inefficient Popping: The pop() operation on a list takes O(1) time on average, 
but it can take O(n) time in the worst case when the underlying array needs to be resized.
"""

"""
Implementing stack using list advantages:
Efficient Popping: collections.deque is implemented as a doubly-linked list, 
and both append and pop operations have O(1) time complexity.
Memory Efficiency: deque may be more memory-efficient than lists for certain use cases.
"""

from collections import deque

class Stack:

    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty(): # check if the stack is already empty
            return self.items.pop()
        else:
            print("Stack is already empty!")

    def show(self):
        print("Stack: ", self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    # to return last item in the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1] 
        else:
            print("Stack is already empty!")

    def size(self):
        return len(self.items)

# creating instance / object of the clas
stack = Stack()

# pushing elements into the stack
stack.push(1)
print(f"pushed {stack.peek()} into the stack")
stack.push(2)
print(f"pushed {stack.peek()} into the stack")
stack.push(3)
print(f"pushed {stack.peek()} into the stack")
stack.push(4)
print(f"pushed {stack.peek()} into the stack")
stack.push(5)
print(f"pushed {stack.peek()} into the stack")
stack.push(6)
print(f"pushed {stack.peek()} into the stack")

# printing stack elements
stack.show()

# peeking last item in the stack
print("Top element: ", stack.peek())

# checking length of the stack
print("Size of the stack: ", stack.size())

# popping elements from stack
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())
print ("popping: ", stack.pop())

# printing stack elements
stack.show()

