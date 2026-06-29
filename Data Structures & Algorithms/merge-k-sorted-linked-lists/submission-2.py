# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        freqDict = {}
        if len(lists) < 1:
            return

        for each in lists:
            while each:
                print(each.val)
                if(each.val in freqDict):
                    freqDict[each.val] += 1
                else:
                    freqDict[each.val] = 1
                each = each.next

        returnList = ListNode(0)
        current = returnList
        for i in range(min(freqDict.keys()), max(freqDict.keys()) + 1):
            if i in freqDict:
                for count in range(freqDict[i]):  # Loop based on the frequency
                    current.next = ListNode(i)  # Add a node with the value `i`
                    current = current.next  # Move the pointer to the new node
            else:
                continue

        # Debug: print the frequency dictionary
        print(f"Frequency Dictionary: {freqDict}")
        return returnList.next


        
            