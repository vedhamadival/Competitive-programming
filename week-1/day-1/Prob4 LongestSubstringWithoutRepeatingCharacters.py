# LongestSubstringWithoutRepeatingCharacters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        m = 0
        sub = {}

        for i , v in enumerate(s):
            if v in sub and start <= sub[v]:
                start = sub[v] + 1 
            else:
                m = max(m , i - start + 1)
            sub[v] = i
        
        return m 
        