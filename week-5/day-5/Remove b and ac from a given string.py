def stringFilter(s):
    ans = ""
    n = len(s) 
    s1 = s.replace('b', '#')
    s2 = s1.replace('ac', '#')

    for i in s2:
        if i != '#':
            ans += i
    
    return ans

str = input() 
print(stringFilter(str))