# my original answer: works but is slow for a few cases where string is extremely long
# this function works by finding the farthest apart matching letters as head-tail pairs and seeing if their "insides" mirror
# ex: s = abba s[0] and s[-1] would be a head-tail pair that is eligible for checking "insides"

def longestPalindrome(s: str) -> str:
    lp = s[0]
    for j in range(len(s)):
        for i in range(-1, -len(s) - 1, -1):            # decrementing from -1
            if s[i]==s[j]:                              # possible palindrome head-tail pair located
                pp = s[j:i] + s[j]                      # potential palindrome
                if len(lp) > len(s)-j:                  # to save time, return if new larger palindrome impossible
                    return lp
                ppsh = pp[-(len(pp) // 2)::]            # pp second half
                if ppsh[::-1]==pp[0:(len(pp) // 2):]:   # palindrome found by comparing halves
                    if len(pp) > len(lp):               # only update if palindrome is larger
                        lp = pp
    return lp

def tests():
    cases = {"babad":"bab", "cbbd":"bb",'aacabdkacaa': 'aca'}
    for x,y in cases.items():
        result = longestPalindrome(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()

