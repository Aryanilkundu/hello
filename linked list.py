#creating individual nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

#here we are creating the links or reference
class LinkedList(Node):
    def __init__(self):
        self.head = None
#till now this is an empty linked list since the ref of head is none or null
    #code for traversing,
    #first we have to check each node,if it is non empty then acces the data
    #and go to the next node
    def print_LL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n=self.head
            while n != None:
                print(n.data)
                n=n.ref
LL1=LinkedList()
LL1.print_LL()