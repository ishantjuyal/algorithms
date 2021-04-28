"""
Write a function to get Nth node in a Linked List
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
    
    def getNth(self, n):
        count = 0 # Initiate a count to keep check on how many nodes we have covered

        temp = self.head
        while temp:
            if count == n: # If the count is same as index needed, return the data from that node
                return(temp.data)
            count += 1 # In case this is not the node, increase the count.
            # We increase count after loop because index starts from 0
            temp = temp.next

if __name__ == '__main__':
 
    llist = LinkedList()
 
    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)
 
    n = 3
    print("Element at index", n, "is :", llist.getNth(n))