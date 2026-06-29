class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # Early exit if s1 is longer than s2
        if len_s1 > len_s2:
            return False
        
        # Frequency count of s1
        s1_count = Counter(s1)
        
        # Frequency count of the first window in s2
        window_count = Counter(s2[:len_s1])
        
        # If the first window matches the frequency, return True
        if s1_count == window_count:
            return True
        
        # Slide the window across s2
        for i in range(len_s1, len_s2):
            # Add the new character (right end of the window)
            window_count[s2[i]] += 1
            # Remove the old character (left end of the window)
            window_count[s2[i - len_s1]] -= 1
            
            # Remove the character count if it goes to zero (clean up the dict)
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Check if the updated window matches s1_count
            if s1_count == window_count:
                return True
        
        return False