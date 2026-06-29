class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the idea here would again be using two pointers one at i+1 and the other
        # at the end of the array. add all three things together depending on if the
        # result is negitive or positive incremenet or deincrement a pointer.

        # Edge cases
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
                
        return result