from timeit import default_timer as timer

#my solution optimized
def lengthOfLongestSubstring(s: str):
    largest = start = 0  # initialize longest sub-string length (w out repeating characters)
    lssl = ""
    for char in s:
        if char not in lssl:
            lssl += char
            largest = max(largest, len(lssl))
        else:
            lssl = lssl[lssl.index(char) + 1:] + char
    return largest


#my solution
# def lengthOfLongestSubstring(s: str):
#     lssl = start = stop = 0 # initialize longest sub-string length (w out repeating characters)
#     while stop <= len(s)-1: #while stop has not "visited" last char
#         substr = s[start:stop+1]
#         if len(set(substr)) == len(substr): #if no duplicates
#             if len(substr) > lssl: #only updates lssl if len() is greater
#                 lssl = len(substr)
#             stop += 1
#         else:
#             start += 1
#
#     return lssl

# #32ms:
# def lengthOfLongestSubstring(s: str) -> int:
#     m = start = 0
#     d = {}
#     for i, char in enumerate(s): # i = index of char
#         if char in d and d[char] >= start: #if char is duplicate and
#             # d[char] gets the dict-value of the char which in this case is its index
#             start = d[char] + 1 #start at index one to right of duplicate
#         elif i - start + 1 > m: # update m if new largest substring found
#             m = i - start + 1
#         d[char] = i # add char to d or update its value
#     return m

# #50ms
# def lengthOfLongestSubstring(s):
#     ans = 0
#     sub = ''
#     for char in s:
#         if char not in sub:
#             sub += char
#             ans = max(ans, len(sub))
#         else:
#             cut = sub.index(char) #first instance of duplicate char
#             sub = sub[cut + 1:] + char #sub starts at index to right of cut char and appends char to end of it
#     return ans

#testing:
import timeit
def tests():
    cases = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "":0," ":1, "dvdf":3}
    #cases = {"dvdf":3}
    for x,y in cases.items():
        result = lengthOfLongestSubstring(x)
        if result == y:
            print(f"{x} passed: result = {result}")
        else:
            print(f"{x} FAILED: result = {result}, but should be {y}")
    print(f"\nmethod passed {next(iter(cases.keys()))} has runtime of {testTime(cases)}ms\n(average over 100,000 runs)")

def testTime(x):
    runtime = timeit.repeat(lambda: lengthOfLongestSubstring(x), number=1, repeat=100000)
    runtime = (sum(runtime) / len(runtime)) / 0.000001
    runtime = int(round(runtime))
    return runtime

tests()

