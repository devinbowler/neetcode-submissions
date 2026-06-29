class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # This will hold all unique subsets (lists).
        result = []
        
        # --------------------------------------------------------
        #  1) Always include the empty subset
        # --------------------------------------------------------
        result.append([])  
        
        # --------------------------------------------------------
        #  2) For each window size k in [1 .. len(nums)]
        #     we do a depth-first search (DFS) to collect 
        #     all subsets of size k.
        # --------------------------------------------------------
        def dfs_combinations(start_index: int, k: int, current_subset: List[int]):
            # If current_subset has length k, store it and return
            if len(current_subset) == k:
                result.append(current_subset[:])
                return
            
            # Try picking elements from start_index onward
            for i in range(start_index, len(nums)):
                current_subset.append(nums[i])
                
                # Recurse with next index, to fill up to size k
                dfs_combinations(i + 1, k, current_subset)
                
                # Backtrack
                current_subset.pop()
        
        # Enumerate all subset sizes from 1 up to len(nums)
        for window_size in range(1, len(nums) + 1):
            dfs_combinations(0, window_size, [])
        
        return result
