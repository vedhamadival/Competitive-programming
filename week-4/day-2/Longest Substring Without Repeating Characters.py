# Use print() to print to the console
def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
 
str = input()
if str==" ":
    print(0)
else:
    print(lengthOfLongestSubstring(str))
