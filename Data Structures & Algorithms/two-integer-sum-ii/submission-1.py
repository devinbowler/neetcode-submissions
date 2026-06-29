class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-indexed indices
                
            elif current_sum < target:
                left += 1
                
            else:
                right -= 1
        
        # If no solution found (should not happen as per problem statement)
        return []