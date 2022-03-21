#my solution
def lengthOfLongestSubstring(s: str):
    lssl = start = stop = 0 # initialize longest sub-string length (w out repeating characters)
    while stop <= len(s)-1: #while stop has not "visited" last char
        substr = s[start:stop+1]
        if len(set(substr)) == len(substr): #if no duplicates
            if len(substr) > lssl: #only updates lssl if len() is greater
                lssl = len(substr)
            stop += 1
        else:
            start += 1

    return lssl

#32ms:
# def lengthOfLongestSubstring(s: str) -> int:
#     m = start = 0 #init m and start to 0
#     d = {}
#     for i, val in enumerate(s): # i = index of val
#         print(d)
#         if val in d:# and d[val] >= start:
#             start = d[val] + 1
#             print(start)
#         elif i - start + 1 > m: # update return val if new larger one yeah yeah
#             m = i - start + 1
#         d[val] = i
#     return m

#50ms
# def lengthOfLongestSubstring(s):
#     ans = 0
#     sub = ''
#     for char in s:
#         if char not in sub:
#             sub += char
#             ans = max(ans, len(sub))
#         else:
#             cut = sub.index(char)
#             #print(f"cut={cut}")
#             sub = sub[cut + 1:] + char
#             #print(f"sub={sub}")
#     return ans

#testing:
def tests():
    cases = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "":0," ":1}
    for x,y in cases.items():
        result = lengthOfLongestSubstring(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()
