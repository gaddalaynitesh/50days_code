class node():
    # function to intialize the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # intialization of the next to null
class linked_list():  # cr
    def __init__(self):
        self.head = None # assigning head to null
    # print function basically traversing through the list
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    ll = linked_list()
    ll.head = node(1)
    second = node(2)
    third = node(3)

    ll.head.next = second;  # Link first node with second
    second.next = third;  # Link second node with the third node

    ll.printlist()