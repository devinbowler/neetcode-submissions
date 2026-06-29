class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        check = len(nums) - k
        while check != 0:
            heapq.heappop(minHeap)
            check -= 1

        return heapq.heappop(minHeap)