"""
Write a function that counts the number of times a given int occurs in a Linked List
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
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = "-> ")
            temp = temp.next
        print("NULL")
    
    def count_n(self, n):
        count = 0
        temp = self.head

        while temp:
            if temp.data == n:
                count += 1
            temp = temp.next
        return(count)

        

if __name__ == '__main__':
 
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    
    n = 1

    # Check for the count function
    print("Count of", n ,"is:", llist.count_n(n))