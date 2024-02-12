class Node():
    def __init__(self, value=0):
        self.value = value
        self.next = None
        
        
class LinkedList():
    def __init__(self, value = None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
                
    def print_list(self):
        '''Print the list.'''
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value: int):
        '''Add a new node at the end.'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1    
        
    def prepend(self, value: int):
        '''Add new node to the beginning.'''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        return True    
            
    def pop_first(self):
        '''Remove node at the beginning.''' 
        if self.length == 0:
            return None 
        else:  
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
        
    def get(self, index: int):
        if index > 0 and index <= self.length:     
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        return None
    
    def set_value(self, index: int, value: int):
        '''Change node's value.'''
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False           
            
    def find(self, target: int):
        '''Get the index of that value.'''
        now = self.head
        index = 0
        while now:
            if now.value == target:
                return index
            now = now.next
            index += 1
        return False
   
    def middle(self):
        '''Find middle node.'''
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isLoop(self):
        '''Check for loop.'''
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False               
 
 
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None  
            
        while temp: # or for _ in range(self.length):
            after = temp.next    
            temp.next = before  
            before = temp
            temp = after 
            
 
    def swap_in_pairs(self):
        '''Swap every two adjacent nodes.
        Input: [1, 2, 3, 4]
        Output: [2, 1, 4, 3]
        '''
        dummy = Node()
        dummy.next = self.head
        pre = dummy
        
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            
            pre.next = second
            first.next = second.next
            second.next = first
    
            pre = first
        return True
    
    
    def delete(self, target):
        '''Delete the first node has that value.'''
        now = self.head
        if now and now.value == target:
            return self.pop_first()
        pre = None
        while now and now.value != target:
            pre = now
            now = now.next
            
        if now is None:
            return False
        pre.next = now.next
        self.length -= 1
        return True
            
            
    def delete_all(self, target):
        '''Delete all the nodes that has that value.'''
        dummy = Node()
        dummy.next = self.head
        now = dummy
        while now.next:
            if now.next.value == target:
                now.next = now.next.next
            else:
                now = now.next
        return True       
    
    
    def remove_duplicates(self):  
        '''Remove duplicates only.'''
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
        return True            
            
            
    def remove_all_duplicates(self):
        '''Remove duplicates and the value that has duplicates.
        NOTE: the linked list has to be sorted first.
        '''   
        temp = Node()
        temp.next = self.head  
        now = temp
        
        while now.next and now.next.next:
            if now.next.value == now.next.next.value:
                remove_value = now.next.value
                while now.next and now.next.value == remove_value:
                    now.next = now.next.next    
            else:
                now = now.next
        return True
  
            
    def pop(self):
        '''Remove the last node.'''
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
        return temp 
    
        
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
        '''Remove at index.'''
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
    
    
    def reverse_between(self, x, y):
        '''x and y are INDEXES.
        Linked list : 3, 8, 5, 10, 2
        with x = 2, y = 4. 
        Output : 3, 8, 2, 10, 5.
        '''
        
        if self.length == 0 or self.length == 1:
            return None
        dummy = Node()
        dummy.next = self.head
        pre = dummy
        for _ in range(x): 
        # change to (x - 1) if you don't want x, y to be indexes.
            pre = pre.next
        now = pre.next
        
        for _ in range(y - x):
            # temp is the next node to be reversed.
            temp = now.next  
            # Disconnect temp, point now after it.
            now.next = temp.next
            # Insert temp at new position after pre.
            temp.next = pre.next
            # Link pre to temp.
            pre.next = temp
        # Update list head if x = 0.   
        self.head = dummy.next    
        
        # Visual example for each step of the first iteration:
        #   8   ->   5   ->  10   ->   2
        #  pre      now     temp    temp.next
        
        #   8   ->   5   ->   2       10      
        #  pre      now              temp
        
        #   8   ->  10   ->   5   ->   2
        #  pre     temp      now   
        

    def partition_list(self, x):
        '''Rearrange the elements in the linked list : nodes with values less 
        than x appear before nodes with values greater than or equal to x.'''
        # the linked list relative order remains unchanged.
        
        if self.head is None:
            return None
        head_1 = Node()
        head_2 = Node()
        # to create two separate linked lists with Node(0) as the head. 
        # elements less than x (less). 
        # elements greater than or equal to x (more).

        less = head_1
        more = head_2
        # used to traverse and build the two partitions.
        now = self.head
        
        while now is not None:
            if now.value < x:
                less.next = now
                less = now
            else:
                more.next = now
                more = now
            now = now.next
            
        less.next = head_2.next
        more.next = None
        self.head = head_1.next     
        
        
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
   


def odd_even(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return
    else:
        pass


def rotate(linked_list, k):
    '''Rotate the list to the right by k places.
    Input: [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]
    '''
    if not linked_list.head or k < 0:
        return False
    elif not linked_list.head.next or k == 0:
        return True
    
    k = k % linked_list.length
    # k = 0 -> no rotation is needed.
    if k == 0:
        return True
    # Fastest approach:
    # Traverse to the node at position length - k % length - 1.
    
    now = linked_list.head
    for _ in range(linked_list.length - k - 1):
        now = now.next
    new_head = now.next
    now.next = None
    linked_list.tail.next = linked_list.head
    linked_list.head = new_head
    return True
 
   
def binary_to_decimal(linked_list):
    '''
    Input: head = [1, 0, 1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    '''
    decimal_value = 0
    now = linked_list.head
    while now:
        # the exponentiation operator (**) to compute the power of 2.
        decimal_value = decimal_value * 2 + now.value
        now = now.next
    return decimal_value
   
   
def cycle(linked_list):
    '''check for cycle in the linked list.'''
    if not linked_list.head or not linked_list.head.next: 
        return False
    slow = linked_list.head
    fast = linked_list.head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    # If there's a cycle, the pointers will eventually meet.    
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
    linked_list.length -= 1   
    return value
            
          

    
    
def add2numbers():
    pass
def insertion_sort_list():
    pass
def split():
    pass
def merge():
    pass
def swap():
    pass
def max(): 
    pass
def min():
    pass
def reverse_in_groups():
    pass
def delete_mid():
    pass
def max_twin_sum():
    pass
def insert_GCD():
    pass
def random():
    pass
         
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
                
            
list_1 = LinkedList(1)
list_1.append(13)
list_1.append(5)
list_1.append(40)
list_1.append(35)
list_1.append(4)

list_2 = LinkedList(7)
list_2.append(25)
list_2.append(3)
list_2.append(9)
list_2.append(11)
list_2.append(2)

print(list_1.find())
list_1.print_list()     
     
     
     
     