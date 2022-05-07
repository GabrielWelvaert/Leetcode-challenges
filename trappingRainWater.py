def trap(height):
    ans = 0
    for i in range(1, max(height)+1):
        l = r = 0
        while l < len(height)-1:
            l = r
            if l < len(height) - 1:
                while not height[l] >= i:
                    l += 1
                r = l+1
            if r < len(height) - 1:
                while not height[r] >= i:
                    if r >= len(height) -1:
                        break
                    r += 1
                if height[r] >= i:
                    ans += r - l - 1
    return ans

# def trap(height):
#     ans = 0
#     for i in range(1, max(height)+1):
#         l = r = 0
#         while l < len(height)-1:
#             l = r
#             if l < len(height) - 1:
#                 while not height[l] >= i:
#                     l += 1
#                 r = l+1
#             if r < len(height) - 1:
#                 while not height[r] >= i:
#                     if r >= len(height) -1:
#                         break
#                     r += 1
#                 if height[r] >= i:
#                     ans += r - l - 1
#     return ans


from dataclasses import dataclass
@dataclass
class Case:
    height: list
    output: int

cases = [Case([1,0,0,0,1,0,1,0],4), Case([0,1,0,1,0],1),Case([0,1,0,1,0,0,1,1,1], 3), Case([0,1,0,1,0,0,2,0,0,2,0,1,1], 8),Case([0,1,0,2,1,0,1,3,2,1,2,1],6),Case([4,2,0,3,2,5],9)]
# #cases = cases[0:3]
# cases = [cases[3]]

for case in cases:
    res = trap(case.height)
    if res == case.output:
        print(f"test passed with {case.height} output was {case.output}")
    else:
        print(f"test failed with {case.height} output was {res} not {case.output}")