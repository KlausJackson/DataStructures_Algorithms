class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None
        
        
class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next    
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 1:
            self.head = self.tail = None
        elif self.length == 0:
            return 
        else:
            temp = self.tail
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index >= 0 and index < self.length:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.pre
            return temp
        return None
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index >= 0 and index <= self.length:
            if index == 0:
                return self.prepend(value)
            elif index == self.length:
                return self.append(value)
            else:
                new_node = Node(value)
                temp = self.get(index)
                before = temp.pre
                new_node.next = temp
                new_node.pre = before
                before.next = new_node
                temp.pre = new_node
        return False
        
    def remove(self, index):
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        