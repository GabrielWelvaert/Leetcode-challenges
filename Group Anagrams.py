from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list) #map char count to list of anagrams

    for s in strs:
        count = [0] * 26 # a to z

        for c in s:
            count[ord(c)-ord("a")] += 1

        res[tuple(count)].append(s)
    return res.values()

def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c)-ord('a')] += 1

        if tuple(count) in res:
            res[tuple(count)].append(s)
        else:
            res[tuple(count)] = [s]
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

