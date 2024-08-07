# Last In First Out - LIFO.

class Node():
    def __init__(self, value = 0):
        self.value = value
        self.next = None


class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.height += 1
        
    def pop(self):
        if self.top:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
            return temp
        return 










































