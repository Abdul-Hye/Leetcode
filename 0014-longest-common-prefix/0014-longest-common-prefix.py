class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        a = list(strs[0])
        prefix = ""

        for i in range(len(a)):
            char = a[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char
        
        return prefix