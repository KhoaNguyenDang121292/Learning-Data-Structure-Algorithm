"""
KEY CONCEPT:
    - Use Element + Linked list data structure for Stack
    - Last in First out
    Activities in Stack:
        + Push. (Insert)
        + Pop. (Remove)
        + Peek (Get top element of stack)
        + isEmpty (Check stack is empty or not)
"""
from LinkedList import Element
from LinkedList import LinkedList

class Stack(object):
    def __init__(self, top=None):
        self.top = top
        self.stack = LinkedList(head=top)
    
    # Push in stack <=> Insert head in Linked list
    def push(self, newElement):
        if self.stack.head:
            temp = self.stack.head
            self.stack.head = newElement
            self.stack.head.next = temp
        else:
            self.stack.head = newElement
    
    # Pop from stack <=> Remove head in Linked list
    def pop(self):
        if self.stack.head:
            self.stack.head = self.stack.head.next
        else:
            self.stack.head = None    

    # Print stack
    def print(self):
        if self.stack.head:
            current = self.stack.head
            while current.next:
                print(str(current.value) + "->", end='')
                current = current.next
        else:
            print(self.stack.head)
        print(str(self.top.value), end='')

if __name__ == "__main__":
    top = Element(0)
    element_1 = Element(1)
    element_2 = Element(2)
    stack = Stack(top=top)
    stack.push(element_1)
    stack.push(element_2)
    stack.print()
    print("")
    stack.pop()
    stack.print()
    print("")
    element_3 = Element(3)
    stack.push(element_3)
    stack.print()
    print("")
    element_4 = Element(4)
    stack.push(element_4)
    stack.print()
    print("")
    stack.pop()
    stack.print()