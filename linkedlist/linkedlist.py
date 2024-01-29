class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def insert_at_begining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def delete(self, key):
        current = self.head

        # Case 1: Deleting the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Case 2: Deleting a node other than the head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {key} not found.")
            return

        prev.next = current.next
        current = None

        

    def search(self, key):
        current = self.head
        
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        itr = self.head

        while itr is not None:
            print(itr.data, end=" -> ")
            itr = itr.next

        print('None')



linkedList = LinkedList()
linkedList.insert_at_end(10)
linkedList.insert_at_end(20)
linkedList.insert_at_end(30)
linkedList.insert_at_begining(1)
print(linkedList.search(60))
print(linkedList.search(30))
linkedList.display()
linkedList.delete(20)
# linkedList.delete(1)
linkedList.delete(30)
linkedList.display()
# linkedList.delete(30)