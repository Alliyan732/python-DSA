"""
Array:
There are some issues with array that linked list try to solve. if we want to insert any element at any specific location
in array, then it will swap all the elements so the time complexity would be O(n)
Python list is dynamic array

let say initially dynamic array allocated with capacity of 5, when it full and we 
insert another element then a new space with 5*2 mem locations will be allocated to 
some other location in the memory, then these all values would be copied to a new array 

so the overhead is not of only swaping but allocating addresses as well as copying all
the elements from old memory area to new memory area.
So this is not that efficent 
Arrays store data in contigous memory locations 


Linked Lists:
values are stored at random locations but linked through pointers.

benefits: 
1) No pre-allocation of space
2) Insertion is easier
3) no swaping like in array

Complexities:
inserting at begining  = O(1)
deleting at begining   = O(1)
Insert / Delete at end or middle = O(n) - because we have to iterate here
Triversal = O(n)
Accessign element by value = O(n)


""" 


"""
defining the structure of the node, it contains the 
data and the addresses of the next node
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3

itr = node1
while itr is not None:
    print(itr.data, end="->")
    itr = itr.next
print("None")
