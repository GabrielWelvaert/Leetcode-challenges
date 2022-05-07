def threeSum(nums):
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a + nums[l] + nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res
#NOT FINISHED DOESNT WORK

from dataclasses import dataclass
@dataclass
class Case:
    nums: list
    output: list

cases = [Case([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]), Case([],[]), Case([0],[])]

for case in cases:
    if threeSum(case.nums) == case.output:
        print(f"test passed with {case.nums}, output was {threeSum(case.nums)}")
    else:
        print(f"test FAILED with {case.nums}, output was {threeSum(case.nums)} not {case.output}")
