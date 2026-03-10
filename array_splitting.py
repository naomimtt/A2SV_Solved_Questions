n, k = map(int,input().split())
nums = list(map(int, input().split()))
highest = nums[n-1] - nums[0]
gaps = []
for i in range(n-1):
    gaps.append(nums[i+1] - nums[i])
gaps.sort()
for i in range(k-1):
    highest -= gaps.pop()
print(highest)
