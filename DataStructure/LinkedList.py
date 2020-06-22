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
            current.next.next = None
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
        prevElement = None
        if self.head:
            current = self.head
            while current.next:
                if count == position - 1:
                    prevElement = current
                if count == position:
                    prevElement.next = newElement
                    temp = current
                    current = newElement
                    current.next = temp
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

    def getMiddleElement(self):
        count = 0
        temp = 0
        if self.head:
            current = self.head
            while current.next:
                current = current.next
                count += 1
        if self.head:
            current = self.head
            while current.next:
                if temp == count//2:
                    return current
                current = current.next
                temp += 1

    def getElementWithPosition(self, position):
        count = 0
        if self.head:
            current = self.head
            while current.next:
                if count == position:
                    return current
                count += 1
                current = current.next
        return None

    def deleteAll(self):
        if self.head:
            current = self.head
            while current.next:
                current.value = None
                current = current.next
    
    def countElementValue(self, element):
        count = 0
        if self.head:
            current = self.head
            while current.next:
                if element.value == current.value:
                    count += 1
                current = current.next
        return count

    def reverse(self):
        # Set previous element as None
        prevElement = Element(None)
        if self.head:
            current = self.head
            while current.value is not None:
                nextElement = current.next
                current.next = prevElement
                prevElement = current
                current = nextElement
            self.head = prevElement

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
            if current.value == None:
                print("NULL")
            else:
                print(str(current.value))


if __name__ == "__main__":
    head = Element(1)
    node_1 = Element(2)
    node_2 = Element(3)
    node_3 = Element(4)
    node_4 = Element(None)
    llist = LinkedList(head=head)
    newHead = Element(0)
    llist.insertHead(newHead)
    llist.insertHead(node_2)
    llist.insertHead(node_3)
    llist.insertTail(node_4)
    llist.traverse()
    position = 2
    newElement_Pos = Element(10)
    newPos = 2
    llist.insertWithPosition(newElement_Pos, newPos)
    llist.traverse()
    middleElement = llist.getMiddleElement()
    print("Middle element: " + str(middleElement.value))
    pospos = 4
    elementPos = llist.getElementWithPosition(pospos)
    print("Element with position " + str(pospos) + ": " + str(elementPos.value))
    # llist.deleteAll()
    # llist.traverse()
    elementToCount = Element(1)
    countElement = llist.countElementValue(elementToCount)
    print("Count element " + str(elementToCount.value) + ": " + str(countElement))
    llist.reverse()
    print("After reverse linked list: ")
    llist.traverse()
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]