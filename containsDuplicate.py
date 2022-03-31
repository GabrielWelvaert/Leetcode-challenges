def containsDuplicate(nums):
    d = {} # key:value hash map
    for i,n in enumerate(nums):
        if n in d:
            return True
        d[n] = i
    return False
    #or return len(nums) != len(set(nums))


def tests():
    cases = {True:[1,2,3,4,5,6,7,8,9,1]}
    for x,y in cases.items():
        result = containsDuplicate(y)
        if result == x:
            print(f"Test passed with {y}: output was {result}")
        else:
            print(f"Test failed with {y}: output was {result} but should have been {y}")

tests()