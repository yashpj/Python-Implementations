class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.dict = dict()
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if len(self.dict)>=self.capacity:
                self.deleteLastNode()
            node = ListNode(key,value)
            self.dict[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        
    
    def deleteLastNode(self):
        if len(self.dict) == 0:
            return
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        del self.dict[temp.key]
        del temp

obj = LRUCache(2)
print(obj.get(1))
obj.put(1,5)
print(obj.get(1))
obj.put(2,2)
obj.put(1,3)
obj.put(3,4)
print(obj.get(3))
print(obj.get(2))


