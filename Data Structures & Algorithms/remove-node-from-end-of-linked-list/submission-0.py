# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newArray = []

        while head:
            newArray.append(head.val)
            print("Value added to array,", head.val)
            head = head.next

        if (len(newArray) == 1): 
            return None

        popVal = len(newArray) - n
        newArray.pop(popVal) 
        firstVal = newArray[0]
        newNode = ListNode(firstVal)

        current = newNode

        for i in range(1, len(newArray)):
            insertNode = ListNode(newArray[i])
            current.next = insertNode
            current = current.next


        return newNode