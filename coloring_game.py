tc = int(input())

for _ in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))
    max_value = max(nums)
    count = 0
    k = n - 1
    while k > 1:
        i = 0
        j = k-1
        
        while i < j:
            if nums[i] + nums[j] + nums[k] > max(max_value, nums[k] * 2):
                count += (j - i)
                j -= 1
            else:
                i += 1
        k -= 1
    print(count)




