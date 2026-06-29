class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Mean ex - 1, 2, 3, 4, 5, 6, 8, 9 = (4 + 5) / 2 = 4.5
        combine = nums1 + nums2
        combine.sort()
        temp = (len(combine) // 2)
        print(temp)
        print(combine)
        print(combine[temp - 1], combine[temp])
        return combine[len(combine) // 2] if len(combine) % 2 != 0 else float(combine[temp - 1] + combine[temp]) / 2.0
