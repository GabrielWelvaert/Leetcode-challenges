def getSum(a,b):
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= MAX else ~(a ^ mask)



def tests():
    cases = {3:[1,2], 5:[2,3]}
    for x,y in cases.items():
        result = getSum(y[0],y[1])
        if result == x:
            print(f"Test passed with {y}: output was {result}")
        else:
            print(f"Test failed with {y}: output was {result} but should have been {x}")

tests()