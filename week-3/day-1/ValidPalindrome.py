class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(filter(unicode.isalnum, s)).lower()
        return s == s[::-1]
