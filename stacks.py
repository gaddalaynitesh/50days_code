class stack:
    def __init__(self):
        self.items = [] # empty list creation
    def is_empty(self):
        return len(self.items)==0 # it returns empty list
    def push(self,item):
        self.items.append(item)  # inserting elements into list
    def pop(self):
        return self.items.pop() # poping the element list
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
if __name__ == "__main__": # after this line if the class is inherited the below code dosent get executed
    s = stack()    # object creation
    print(s.is_empty())
    s.push(3)    # pushing the first element into list
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop()) # popping element
    print(s.peek()) # returns the last element in the list
