# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], leftC: int, rightC: int) -> Optional[ListNode]:
        
        if leftC == rightC or not head or not head.next:
            return head
        
        preLeft = None
        left = head
        right = None
        postRight = None

        count = 1
        curr = head

        while count < leftC and curr:
            preLeft = curr
            curr = curr.next
            left = curr
            count += 1
        
        while count <= rightC and curr:
            right = curr
            curr = curr.next
            postRight = curr
            count += 1
        

        if right:
            right.next = None

        prev = postRight
        curr = left
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if preLeft:
            preLeft.next = prev
        
        return prev if leftC == 1 else head
        
