class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for i in range(len(pattern)):

            if pattern[i] in p_to_w:
                if p_to_w[pattern[i]] != words[i]:
                    return False
            else:
                p_to_w[pattern[i]] = words[i]

            if words[i] in w_to_p:
                if w_to_p[words[i]] != pattern[i]:
                    return False
            else:
                w_to_p[words[i]] = pattern[i]

        return True