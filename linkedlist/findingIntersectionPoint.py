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

    
    def display(self):
        itr = self.head

        while itr is not None:
            print(itr.data, end=" -> ")
            itr = itr.next

        print('None')
    
    def length(self):
        len = 0
        current = self.head

        while current is not None:
            current = current.next
            len += 1

        return len
    
    def intersection(self):
        len1 = linkedList1.length()
        len2 = linkedList2.length()
        dif = 0

        if len1 > len2:
            dif = len1 - len2
            ptr1 = linkedList1.head
            ptr2 = linkedList2.head
            for i in range(dif):
                ptr1 = ptr1.next
       
        elif len2 > len1:
            dif = len2 - len1
            ptr1 = linkedList1.head
            ptr2 = linkedList2.head
            for i in range(dif):
                ptr2 = ptr2.next
        
        while ptr1 is not None and ptr2 is not None:
            if ptr1.data == ptr2.data:
                return ptr1.data
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        
        print("There is no point of intersection")
        


linkedList1 = LinkedList()
linkedList1.insert_at_end(1)
linkedList1.insert_at_end(2)
linkedList1.insert_at_end(3)
linkedList1.insert_at_end(4)
linkedList1.insert_at_end(5)
linkedList1.insert_at_end(6)
linkedList1.display()
print("linkedList1 length: ",linkedList1.length())

linkedList2 = LinkedList()
linkedList2.insert_at_end(9)
linkedList2.insert_at_end(10)
linkedList2.insert_at_end(5)
linkedList2.insert_at_end(6)
linkedList2.display()
print("linkedList2 length: ",linkedList2.length())


print("Point of Intersection: ",LinkedList().intersection())