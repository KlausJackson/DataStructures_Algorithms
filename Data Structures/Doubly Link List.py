''' Notable usages:
    - Bi-directional traversal. 
    - Efficient deletion of a node. 
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None
        
        
class LinkedList():
    '''Doubly Linked List'''
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
                self.length += 1
        return False
        
    def remove(self, index):
        if index >= 0 and index < self.length:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            else:
                # temp.next.pre = temp.pre
                # temp.pre.next = temp.next
                temp = self.get(index)
                before = temp.pre
                after = temp.next
                before.next = after
                after.pre = before
                temp.next = temp.pre = None
                self.length -= 1
                return temp
        return         
        
    def swap_first_last(self):
        '''Swap the values of the first and last node.'''    
        if not self.head or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True
     
    def reverse(self):
        if not self.head:
            return
        temp = self.head
        while temp:
            temp.pre, temp.next = temp.next, temp.pre
            # because temp.pre = temp.next 
            # so to move to the next node
            temp = temp.pre
        self.head, self.tail = self.tail, self.head             
        return True
        
    def palindrome(self):
        if self.length == 1:
            return True
        start = self.head
        end = self.tail
        # // largest integer that is less than/equal to the result.
        for _ in range(self.length // 2):
            if start.value != end.value:
                return False
            start = start.next
            end = end.pre
        return True
    
    
    def swap_in_pairs(self):
        if not self.head:
            return 
        dummy = Node()
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            second.pre = prev
            first.pre = second
            
            # if there's a node after 'first',
            # update its 'pre' to point back to 'first'.
            if first.next:
                first.next.pre = first
            prev = first
        
        self.head = dummy.next    
        return True
        
        
        
test = LinkedList(2)
test.append(6)
test.append(3)
test.append(11)      
 
        
   