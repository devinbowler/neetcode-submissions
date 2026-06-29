class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, o, t = 0, 0, 0
        for each in nums:
            if each == 0:
                z += 1
            elif each == 1:
                o += 1
            else:
                t += 1
        
        for idx in range(len(nums)):
            if z != 0:
                nums[idx] = 0
                z -= 1
                continue
            
            if z == 0 and o != 0:
                nums[idx] = 1
                o -= 1
                continue
            
            if z == 0 and o == 0 and t != 0:
                nums[idx] = 2
                t -= 1
                continue

        