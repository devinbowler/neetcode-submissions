class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        idx = 0
        minWord = min(strs, key=len)
        match = True
        while match and idx < len(minWord):
            pref += strs[0][idx]
            print(idx)
            for each in strs:
                if each[idx] != pref[idx]:
                    match = False
                    pref = pref[:-1]
                    break
                else:
                    continue
            idx += 1

        return pref
