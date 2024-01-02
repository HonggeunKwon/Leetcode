# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        deq = collections.deque()
        
        while head is not None:
            deq.append(head.val)
            head = head.next
        
        while len(deq) > 1:
            if deq.pop() != deq.popleft():
                return False
        return True