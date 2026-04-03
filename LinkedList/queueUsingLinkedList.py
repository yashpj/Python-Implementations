class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, music):
        node = Node(music)
        if self.rear:
            self.rear.next = node
            self.rear = self.rear.next
        else:
            self.front = node
            self.rear = node
    
    def dequeue(self):
        if self.front:
            node = self.front
            self.front = self.front.next
            return node.value
        else:
            return None
    
    def peek(self):
        if self.front:
            node = self.front
            return node.value
        else:
            return None

    
    
# Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 