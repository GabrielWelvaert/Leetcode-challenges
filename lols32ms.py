def lengthOfLongestSubstring(s: str) -> int:
    m = start = 0 #init m and start to 0
    d = {}
    for i, val in enumerate(s): # i = index of val
        print(d)
        if val in d:# and d[val] >= start:
            start = d[val] + 1
            print(start)
        elif i - start + 1 > m: # update return val if new larger one yeah yeah
            m = i - start + 1
        d[val] = i
    return m

def tests():
    cases = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "":0," ":1, "abba":2}
    cases = {"tmmzuxt":5}
    for x,y in cases.items():
        result = lengthOfLongestSubstring(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()
