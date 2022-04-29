
# O(n) solution
def longestConsecutive(nums):
    lcs = 0
    numSet = set(nums)
    for n in nums:
        #check if start of sequence, does n-1 exist in numSet
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            lcs = max(length, lcs)
    return lcs

#my soltuion: O(nlogn) because sort()
# def longestConsecutive(nums):
#     lcs = current = 0
#     if not nums: return 0
#     nums = set(nums)
#     nums = [i for i in nums]
#     nums.sort()
#     for i in range(len(nums)-1):
#         if nums[i] == nums[i+1]-1:
#             current += 1
#         else:
#             if current > lcs:
#                 lcs = current
#             current = 0
#     if current > lcs:
#         lcs = current
#     return lcs + 1

class Testing:

    from dataclasses import dataclass

    @dataclass
    class Case:
        nums: tuple
        output: int

    cases = [Case((100,4,200,1,3,2), 4), Case((0,3,7,2,5,8,4,6,0,1), 9), Case(([1,2,0,1]),3), Case(([]),0)]
    #cases = [cases[-1]]

    def Test(self, cases=cases):
        for case in cases:
            ans = longestConsecutive(list(case.nums))
            if ans == case.output:
                print(f'test passed with {case.nums}: output was {ans}')
            else:
                print(f'test FAILED with {case.nums}: output was {ans} not {case.output}')

Testing.Test(Testing)



