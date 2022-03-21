def lengthOfLongestSubstring( s):
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char
            ans = max(ans, len(sub))
        else:
            cut = sub.index(char)
            print(f"cut={cut}")
            sub = sub[cut + 1:] + char
            print(f"sub={sub}")
    return ans

def tests():
    cases = {"abcabcbb":3, "bbbbb":1, "pwwkew":3, "":0," ":1}
    cases = {"abcabcbb":3}
    for x,y in cases.items():
        result = lengthOfLongestSubstring(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()
