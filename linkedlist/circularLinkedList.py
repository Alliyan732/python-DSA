class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:           # check if there is no head node
            self.head = new_node        # then make the new node as head 
            new_node.next = self.head   # making circular link for single node
            return
        
        # else create another pointer current that will iterate through the list
        # this current pointer will initially point the head
        current = self.head 
        while current.next != self.head:  
            current = current.next      # we will keep move to next 
        current.next = new_node         # at the end, adding new node 
        new_node.next = self.head       # making list circular 

    def insert_at_begining(self, data):
        new_node = Node(data)

        if not self.head:               # checking if there is no node present
            self.head = new_node        
            new_node.next = self.head   # next of new node point head, which is itself newnode
        else:
            current = self.head         
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node


        

    def search(self, key):
        current = self.head
        
        while current.next is not self.head:
            if current.data == key or current.next.data == key:
                return True
            current = current.next
        return False

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

    def delete(self, key):
        
        if self.head is None:   # if there is no node
            print("Linked list is empty")
            return
        
        # Case 1: If the node to be deleted is the only node in the list
        if self.head.data == key and self.head.next == self.head:
            self.head = None
            print("Node Deleted")
            return            
        
        # Case 2: If the node to be deleted is the head
        if self.head.data == key and self.head.next != self.head:
            current = self.head

            # linking end node to the head 
            while current.next is not self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next  
            return
        
        # Case 3: If the node to be deleted is not the head
        else:
            prev = None
            current = self.head
            
            while current.next is not self.head:
                prev = current
                current = current.next
                if current.data == key:
                    print("current data: ",current.data)
                    prev.next = current.next
                    print("Key deleted")
                    return
            
        print("Key not found")





linkedList = LinkedList()
linkedList.insert_at_end(10)
linkedList.insert_at_end(20)
linkedList.insert_at_end(30)
linkedList.insert_at_end(40)
linkedList.insert_at_begining(1)
# linkedList.insert_at_begining(100)
print(linkedList.search(30))
print(linkedList.search(120))
linkedList.delete(10)
linkedList.delete(20)
linkedList.delete(40)
linkedList.delete(60)
linkedList.delete(1)
linkedList.display()
