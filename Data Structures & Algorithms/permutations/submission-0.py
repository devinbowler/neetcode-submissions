class TrieNode:
    def __init__(self):
        self.children = {}
        self.permutation = []

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        root = TrieNode()

        def build(node, remaining):
            # Base case: no numbers left to add
            if not remaining:
                return [node.permutation]
            
            results = []
            for num in remaining:
                # Create a child node
                child = TrieNode()
                child.permutation = node.permutation + [num]
                node.children[num] = child
                
                # Recurse with remaining numbers excluding the current one
                results.extend(build(child, [x for x in remaining if x != num]))
            return results

        # Start building the tree from the root
        return build(root, nums)