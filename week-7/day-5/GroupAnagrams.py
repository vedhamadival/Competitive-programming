from collections import defaultdict

def groupAnagram(strs):
    anagramMap = defaultdict(list)
    
    for word in strs:
        sortedWord = ''.join(sorted(word))
        anagramMap[sortedWord].append(word)
    
    groupedAnagram = list(anagramMap.values())
    return groupedAnagram

n = int(input())
strs = input().split(" ")

groupedAnagram = groupAnagram(strs)

arre = []
for group in groupedAnagram:
    arre.append(' '.join(group))
arre.reverse()
for i in arre:
    print(i)
