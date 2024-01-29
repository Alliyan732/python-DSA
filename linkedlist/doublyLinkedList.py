class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:   # check if there is no head node
            self.head = new_node # then make the new node as head 
            return
        
        # else create another pointer current that will iterate through the list
        # this current pointer will initially point the head
        current = self.head 
        while current.next is not None:  # until there is something on current.next, not null
            current = current.next # we will keep move to next 
        current.next = new_node   # at the end, adding new node 
        new_node.prev = current   # settig prev pointer

    def insert_at_begining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode    # setting prev pointer
        self.head = newNode

    def delete(self, key):
        current = self.head

        # case 1: if there is no node present
        if self.head == None:
            print("Linked list is empty")
            return

        # case 2: if the node to be deleted is the head node
        elif key == self.head.data:
            self.head = current.next
            self.head.prev = None
            print("Head Node deleted")
            return

        # case 3: if the node to be deleted is not head node
        else:
            while current.next is not self.head:
                current = current.next
                if current.data == key:
                    current.prev.next = current.next
                    if current.next is not None: # handling last node
                        current.next.prev = current.prev
                        current = None
                    print("Node other than head is deleted")
                    return
        
        print("Node not found")


    def search(self, key):
        current = self.head
        
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print('None')

    def displayReverse(self):
        current = self.head

        while current is not None and current.next is not None:
            current = current.next 
        
        while current is not None:
            print(current.data, end=" -> ")
            current = current.prev
        
        print("None")




linkedList = LinkedList()
linkedList.insert_at_end(10)
linkedList.insert_at_end(20)
linkedList.insert_at_end(30)
linkedList.insert_at_begining(1)
linkedList.insert_at_begining(2)
print(linkedList.search(30))
linkedList.delete(2)
linkedList.delete(10)
linkedList.delete(30)
linkedList.display()
# linkedList.displayReverse()