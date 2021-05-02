"""
Pairwise swap elements of a given linked list
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
    
    def get_list(self):
        new_list = []
        temp = self.head
        while(temp):
            new_list.append(temp.data)
            temp = temp.next
        return(new_list)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")
    
    def swap(self, x, y):
        # Base case if both x and y are same, do nothing
        if x == y:
            return

        # Keeping track of details about node of value x
        prev_x = None
        curr_x = self.head
        while curr_x != None and curr_x.data != x:
            prev_x = curr_x # Storing value of previous node in prev_x
            curr_x = curr_x.next
        
        # Keeping track of details about node of value x
        prev_y = None
        curr_y = self.head
        while curr_y != None and curr_y.data != y:
            prev_y = curr_y # Storing value of previous node in prev_y
            curr_y = curr_y.next
        
        # If the data is not found in the Linked List, do nothing
        if curr_x == None or curr_y == None:
            return
        
        # If x is not head of linked list
        if prev_x != None:
            prev_x.next = curr_y
        else:
            self.head = curr_y
        
        # If y is not head of linked list
        if prev_y != None:
            prev_y.next = curr_x
        else:
            self.head = curr_x
        
        # Swap next pointers
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp


if __name__ == '__main__':
    llist = LinkedList()

    # llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Linked list before pairwise swapping")
    llist.printList()
    elements = llist.get_list()
    n = len(elements)
    for i in range(0, n-1, 2):
        llist.swap(elements[i], elements[i+1])
    print("\nLinked list after calling swapNodes() ")
    llist.printList()
    