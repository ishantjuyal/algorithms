"""
Search an element in a Linked List (Iterative and Recursive)
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
    
    # Iterative Approach
    def search(self, node_val):
        val = 0 # Initialize a variable to check if the node is found or not

        temp = self.head
        while temp:
            if temp.data == node_val: # When the node is found
                val = 1 # Changed the value of val because the node is found, now break out of the loop
                break
            temp = temp.next
        if val == 1:
            return(True)
        else:
            return(False)
    
    # Recursive Approach
    def look_for(self, node, key):
        if (not node):
            return(False)
        
        if node.data == key:
            return(True)
        else:
            return(self.look_for(node.next, key))


# Code execution starts here
if __name__ == '__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    search_val = 14
    print("Result from Iterative Approach:", llist.search(search_val))
    print("Result from Recursive Approach:", llist.look_for(llist.head, search_val))
