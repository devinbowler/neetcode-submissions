# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        
        
        while curr is not None:
            count += 1
            curr = curr.next
        
        if(count == 1):
            return None

        newCurr = head
        returnNode = None
        currentNewNode = None

        for i in range(count):
            if(i == count - (n)):
                newCurr = newCurr.next
                continue
            
            else:
                if returnNode is None:
                    returnNode = ListNode(newCurr.val)
                    currentNewNode = returnNode
                else:
                    currentNewNode.next = ListNode(newCurr.val)
                    currentNewNode = currentNewNode.next
                newCurr = newCurr.next

        return returnNode
