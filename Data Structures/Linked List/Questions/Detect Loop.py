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
    
    def detect(self):
        node_list = []
        temp = self.head
        loop = False
        while temp:
            if temp not in node_list:
                node_list.append(temp)
            else:
                loop = True
                break
        return(loop)




if __name__ == '__main__':
 
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    
    if(llist.detect()):
        print("Loop found")
    else:
        print("No Loop ")