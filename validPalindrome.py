#using pointers to be memory efficient (mem = O(1))
def isPalindrome(s): #left and right pointer inching inward solution

    def alphaNum(c): #helper method for checking if alphanumeric
        return ("a" <= c.lower() <= "z") or ("0" <= c <= "9") #checks ascii values!

    l = 0
    r = len(s) -1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

#easy pythonic, but uses extra memory
def isPalindrome(s):
    if not s: return True
    s2 = ""
    for c in s:
        if c.isalnum():
            s2 += c.lower()
    return s2 == s2[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))