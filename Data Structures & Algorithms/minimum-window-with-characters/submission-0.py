class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        stringT, stringWindow = {}, {}

        for c in t:
            stringT[c] = 1 + stringT.get(c, 0)
        
        have, need = 0, len(stringT)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        for r in range(len(s)):
            c = s[r]
            stringWindow[c] = 1 + stringWindow.get(c, 0)
            if c in stringT and stringT[c] == stringWindow[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                stringWindow[s[l]] -= 1
                if s[l] in stringT and stringWindow[s[l]] < stringT[s[l]]:
                    have -= 1 

                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float('infinity') else ""


        return res