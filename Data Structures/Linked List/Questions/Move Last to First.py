"""
Move last element to front of a given Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return(count)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")
    
    def move(self):
        first = self.head
        temp = self.head
        while temp:
            if temp.next.next == None:
                last = temp.next
                temp.next = None
            temp = temp.next
        last.next = first
        self.head = last


if __name__ == '__main__':
    llist = LinkedList()
      
    # swap the 2 nodes
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print ("Linked List before moving last to front ")
    llist.printList()
    llist.move()
    print ("Linked List after moving last to front ")
    llist.printList()
