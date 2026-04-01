class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    newHead = dummy
    c = 0
    
    while head_a or head_b:
        
        val_a = head_a.value if head_a else 0
        val_b = head_b.value if head_b else 0
        
        sum = val_a + val_b + c
        
        dummy.next = Node(sum%10)
        dummy = dummy.next
        
        c = sum//10
        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next
    
#    while head_a:
        
 #       dummy.next = Node(head_a.value)
  #      dummy = dummy.next
  #      head_a = head_a.next
    
 #   while head_b:
   #     dummy.next = Node(head_b.value)
    #    dummy = dummy.next
    #    head_b = head_b.next
    return newHead.next

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))



        
