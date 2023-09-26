class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_el = min(strs, key=len)
        strs = sorted(strs)
        for j in range(0,len(min_el)):
            if strs[0][j] != strs[-1][j]:
                break
            output += strs[0][j]            
        return output