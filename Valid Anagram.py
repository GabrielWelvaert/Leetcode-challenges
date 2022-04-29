def isAnagram(s,t): #pythonic one-liner, not as efficient as below
    return sorted(s) == sorted(t)


def isAnagram(s,t): #hashmap solution with letter:instances of letter
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)): #use .get to avoid keyerrors when hashmap is empty
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

from collections import Counter
def isAnagram(s, t): #Counter solution, does same as above
    return Counter(s) == Counter(t)

def isAnagram(s, t):
    if len(s) != len(t): return False
    countS, countT = {}, {}

    for i in range(len(s)):
        if s[i] not in countS:
            countS[s[i]] = 0
        countS[s[i]] += 1
        if t[i] not in countT:
            countT[t[i]] = 0
        countT[t[i]] += 1

    return countS == countT

print(isAnagram("abc","cba"))

