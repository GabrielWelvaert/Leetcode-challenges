def lengthOfLongestSubstring(s: str):
    largest = start = 0
    lssl = ""
    for char in s:
        if char not in lssl:
            lssl += char
            largest = max(largest, len(lssl))
        else:
            lssl = lssl[lssl.index(char) + 1:] + char
    return largest


