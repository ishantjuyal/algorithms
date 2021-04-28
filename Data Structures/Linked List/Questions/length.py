"""
Find Length of a Linked List (Iterative and Recursive)
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
    
    # Iterative approach
    def get_length(self):
        count = 0 # Initiate a count

        temp = self.head
        while temp: # Traverse through the Linked List
            count += 1 # Change the count to know how many nodes have been counted
            temp = temp.next
        return(count)
    
    # Recursive approach
    def get_count_rec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.get_count_rec(node.next)
    def get_count(self):
        return self.get_count_rec(self.head)


# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print ("Count of nodes by iterative approach is :",llist.get_length())

    print ("Count of nodes by recursive approach is :",llist.get_count())