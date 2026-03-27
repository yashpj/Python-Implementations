class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("None")
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    
    curr = head
    dummy = Node(0)
    newHead = dummy
    
    while curr:
        
        if curr.next and curr.value == curr.next.value:
            dupli = curr.value
            
            while curr.next and curr.value == dupli:
                curr = curr.next
            continue
        else:
            dummy.next = Node(curr.value)
            dummy = dummy.next
            curr = curr.next
    return newHead.next
        

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
print_linked_list(delete_dupes(head))

