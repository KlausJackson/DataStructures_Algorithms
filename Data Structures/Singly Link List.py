class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
                
    def print_list(self):
        '''print the list'''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        '''add a new node at the end'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1    
        
            
    def pop(self):
        '''remove the last node'''
        if self.length == 0:
            return None
        temp = pre = self.head  
             
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None   
             
        self.length -= 1
        return temp # or temp.value.
    
        
    def prepend(self, value):
        '''add new node to the beginning'''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        return True    
            
    def pop_first(self):
        '''remove node at the beginning''' 
        if self.length == 0:
            return None 
        else:  
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
        
    def get(self, index):
        if index < 0  or index >= self.length:    
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        '''change node's value'''
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
        
    def insert(self, index, value):
        if index < 0  or index > self.length:    
            return False        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            # not self.length - 1 
            # because self.length is the last position.
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)   
        new_node.next = temp.next
        temp.next = new_node       
        self.length += 1
        return True
    
            
    def remove(self, index):
        if index < 0  or index >= self.length:    
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
                  
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return True
    
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        
        for _ in range(self.length):
            after = temp.next    
            temp.next = before  
            before = temp
            temp = after
            
   
    def middle(self):
        '''find middle node'''
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isLoop(self):
        '''check for loop'''
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    
    def partition_list(self, x):
        '''rearrange the elements in the linked list : nodes with values less 
        than x appear before nodes with values greater than or equal to x.'''
        # the linked list relative order remains unchanged.
        
        if self.head is None:
            return None
        head_1 = Node(0)
        head_2 = Node(0)
        # to create two separate linked lists with Node(0) as the head. 
        # elements less than x (k). 
        # elements greater than or equal to x (j).

        less = head_1
        more = head_2
        # used to traverse and build the two partitions.
        current = self.head
        
        while current is not None:
            if current.value < x:
                less.next = current
                less = current
            else:
                more.next = current
                more = current
            current = current.next
            
        less.next = head_2.next
        more.next = None
        self.head = head_1.next     
        
        
    def remove_duplicate(self):  
        # set() : built-in data type,  unordered collection of unique elements. 
        # Example: {8, 7, 3, 11, 5}
        # Uniqueness: try to add a duplicate, it will not be included.
        # Unordered: cannot access elements by index.
        # Mutable: can add and remove elements.
        # Operations: union, intersection, difference, and symmetric difference.
        
        exist_values = set()
        pre = None
        now = self.head
        while now:
            if now.value in exist_values:
                pre.next = now.next
                self.length -= 1
            else:
                exist_values.add(now.value)
                pre = now
            now = now.next
            
        
    def isPalindrome(self):
        '''check for palindrome'''
        if not self.head or not self.head.next:
            return True
        mid = self.middle()
        # Reverse the second half of the linked list
        next_half = None
        
        while mid:
            # point temp to mid.next.
            temp = mid.next
            # point mid to the node before it (this step reverse the pointer).
            mid.next = next_half
            # update the next_half and mid pointer to the node after it
            # in the second half to continue reverse the pointer.
            next_half = mid
            mid = temp
            
            # Visual example of pointer's orders in the beginning:
            # None     <-    10          5          21
            #   ^            ^           ^          ^
            # next_half     mid         temp        temp 
            #               next_half    mid        temp    (in the next iteration)
   
        while next_half:
            now = self.head
            if now.value != next_half.value:
                return False
            now = now.next
            next_half = next_half.next
        return True    
   
   
def find_kth_from_end(linked_list, k):
    '''takes the LinkedList and integer k, returns the k-th node 
    from the end of the linked list. WITHOUT USING LENGTH'''
        
    # reason why:
    # Using length requires traversing the entire list once to find 
    # its length (if index < 0  or index >= self.length)
    # and then traversing it again to reach the desired node.

    # The two-pointer approach : one traverse through the linked list. 
    # Fast moves k nodes first to check if k is out of bound. 
    # After fast is k nodes ahead of slow, now both move at the same pace.
    # When fast reaches the end, the slower pointer will be at the Kth node 
        
    # 5 - 4 = 1 and 5 - 1 = 4
    # linklist : 1, 2, 3, 4, 5
    # k = 2
    # find_kth_from_end(linklist, k) -> 4
        
    slow = fast = linked_list.head
    index = 0
    for _ in range(k):        
        if not fast:
            return None
        fast = fast.next
    if not fast:
        return linked_list.get(0).value, 0 
        
    while fast:
        slow = slow.next
        fast = fast.next
        index += 1
        # when fast reaches the end, it's still True, not None yet.
        # when slow is at the kth node, fast is None, the loop stops.
    
    # get the value and its index for other purposes (remove, set_value, etc).
    return slow.value, index
    
    
def remove_kth_from_end(linked_list, k):
    if k < 0:
        return None
    slow = fast = linked_list.head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
        
    if not fast:  
        return linked_list.pop_first()              
    while fast.next:
        slow = slow.next
        fast = fast.next
    value = slow.next.value
    slow.next = slow.next.next    
    return value
                
            
ll = LinkedList(1)
ll.append(13)
ll.append(5)
ll.append(40)
ll.append(35)
ll.append(4)

print(find_kth_from_end(ll, 7))
print('list:')
ll.print_list()     
     
     
     
     
     
      
     
     
     