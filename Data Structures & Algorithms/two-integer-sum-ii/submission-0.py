class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in numMap:
                return [numMap[complement] + 1, i + 1]
            
            numMap[num] = i

        print(numMap)
        return []