def longestPalindrome(s: str) -> str:
    lp = ""
    return lp



#testing:
def tests():
    cases = {"babad":"bab", "cbbd":"bb"}
    for x,y in cases.items():
        result = longestPalindrome(x)
        if result == y:
            print(f"Test passed with {x}: output was {result}")
        else:
            print(f"Test failed with {x}: output was {result}")

tests()