""" KEY CONCEPT:
    1. Each element has: value and next element
    2. Each linked list when adding:
        - Check if HEAD exists.
        - Iterate until end of linked list and then add new element.
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
         
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def add(self, newElement):
        # Check if linkedlist already had HEAD
        if self.head:
            current = self.head
            # Iterate to end of this linked list
            while current.next:
                current = current.next
            # Add new element next to last element
            current.next = newElement
        else:
            self.head = newElement
    
    def traverse(self):
        # Check if Linked list already had HEAD
        if self.head:
            current = self.head
            # Iterate to end of this linked list
            while current.next:
                # Print current node value
                if current.next:
                    if current == self.head:
                        print("HEAD<--" + str(current.value) + "->", end='')
                    else:
                        print(str(current.value) + "->", end='')
                else:
                    print(str(current.value), end='')
                current = current.next


if __name__ == "__main__":
    head = Element(1)
    node_1 = Element(2)
    llist = LinkedList(head=head)
    llist.add(node_1)
    llist.traverse()
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    