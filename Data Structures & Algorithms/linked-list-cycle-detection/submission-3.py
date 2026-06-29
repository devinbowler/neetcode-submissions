# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point1 = head
        point2 = head
        while point2 and point2.next:
            point1 = point1.next
            point2 = point2.next.next
            if point1 is point2:
                return True

        return False