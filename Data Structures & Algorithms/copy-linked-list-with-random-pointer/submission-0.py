"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashForOld = { None : None }

        cur = head
        while cur:
            copyNode = Node(cur.val)
            hashForOld[cur] = copyNode
            cur = cur.next

        cur = head
        while cur:
            copy = hashForOld[cur]
            copy.next = hashForOld[cur.next]
            copy.random = hashForOld[cur.random]
            cur = cur.next


        return hashForOld[head]