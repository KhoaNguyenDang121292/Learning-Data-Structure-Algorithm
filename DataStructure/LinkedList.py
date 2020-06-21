""" KEY CONCEPT:
    1. Each element has: value and next element
    2. Each linked list when adding:
        - Check if HEAD exists.
        - Iterate until end of linked list and then add new element.
    3. Activities on Linked list:
        - Insert new element on first/last position.
        - Delete first element with a given value.
        - Search (next to what element)
        - Traverse all elements.
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
         
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insertTail(self, newElement):
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
    
    def insertHead(self, newElement):
        # Check if linkedlist already had HEAD
        if self.head:
            temp = self.head
            self.head = newElement
            self.head.next = temp
        else:
            self.head = newElement

    def insertWithPosition(self, newElement, position):
        count = 0
        if self.head:
            current = self.head
            while current.next:
                if count == position:
                    temp = current
                    current = newElement
                    current.next = temp
                    break
                current = current.next
                count += 1
        else:
            current = newElement

    def getPosition(self, position):
        count = 0
        if self.head:
            current = self.head
            while current.next:
                if count == position:
                    return current
                current = current.next
                count += 1
            return None
    
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
            print(str(current.value))


if __name__ == "__main__":
    head = Element(1)
    node_1 = Element(2)
    node_2 = Element(3)
    node_3 = Element(4)
    llist = LinkedList(head=head)
    newHead = Element(0)
    llist.insertHead(newHead)
    llist.insertHead(node_2)
    llist.insertHead(node_3)
    llist.traverse()
    position = 2
    newElement_Pos = Element(10)
    newPos = 2
    llist.insertWithPosition(newElement_Pos, newPos)
    llist.traverse()
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]