def maxArea(height):
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        top = min(height[l], height[r])
        width = r - l
        ans = max(top * width, ans)
        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
    return ans



from dataclasses import dataclass
@dataclass
class Case:
    height: list
    output: int

cases = [Case([1,8,6,2,5,4,8,3,7],49), Case([1,1],1), Case([2,3,4,5,18,17,6],17)]


for case in cases:
    if maxArea(case.height) == case.output:
        print(f"test passed with {case.height} output was {case.output}")
    else:
        print(f"test failed with {case.height} output was {maxArea(case.height)} not {case.output}")