"""
Find length of loop in linked list
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
    
    def loop_length(self):
        node_list = []
        temp = self.head
        loop = False
        index = 0
        while temp:
            if temp not in node_list:
                node_list.append(temp)
            else:
                new_index = node_list.index(temp)
                loop = True
                break
            temp = temp.next
            index += 1
        
        if loop == True:
            return(index - new_index)
        else:
            return(0)


if __name__ == '__main__':
 
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    

    print("Length of loop in the Linked List:", llist.loop_length())