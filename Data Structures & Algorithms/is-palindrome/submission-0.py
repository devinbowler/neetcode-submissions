class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredNums = []
        for char in s:
            if char.isalnum():
                filteredNums.append(char.lower())
                
        start = 0
        end = len(filteredNums) - 1
        
        while start < end:
            if filteredNums[start] != filteredNums[end]:
                return False
            start += 1
            end -= 1
        
        return True