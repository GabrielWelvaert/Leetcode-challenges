def twoSum(nums, target):
    d = {} #hash map value:index that will store "visisted" values & original index from input list:
    for i, n in enumerate(nums):
        diff = target - n
        if diff in d:
            return [d[diff],i] #return indicies of valid values
        d[n] = i #add n:i to the hash map

print(twoSum([2,1,5,3], 4))
print(twoSum([2,7,11,15], 9))
