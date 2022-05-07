def topKFrequent(nums, k):
    h = {}
    freq =[[] for i in range(len(nums)+1)]

    for n in nums:
        h[n] = 1 + h.get(n, 0)

    for n,c in h.items():
        freq[c].append(n)

    ans = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            ans.append(n)
            if len(ans) == k:
                return ans

print(topKFrequent([1,1,1,2,2,4], 2))
print(topKFrequent([-1,-1],1))
print(topKFrequent([1,2],2))

