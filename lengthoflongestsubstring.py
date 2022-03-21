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


def tests():
    cases = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "":0," ":1}
    for x,y in cases.items():
        result = lengthOfLongestSubstring(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()
