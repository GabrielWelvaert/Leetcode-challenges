def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while  l < r:
        curSum = numbers[l] + numbers[r]
        #remember, input list is already sorted, so this works:
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1,r+1]

from dataclasses import dataclass
@dataclass
class Case:
    numbers: list
    target: int
    output: list

cases = [Case([2,7,11,15],9,[1,2]), Case([2,3,4],6,[1,3]), Case([-1,0],-1,[1,2]), Case([0,0,3,4],0,[1,2])]

for case in cases:
    if twoSum(case.numbers, case.target) == case.output:
        print(f"test passed with {case.numbers}, {case.target}: output was {case.output}")
    else:
        print(f"test failed with {case.numbers}, {case.target}: output was {twoSum(case.numbers, case.target)} not {case.output}")

