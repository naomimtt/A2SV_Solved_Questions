n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
count = 0
curr_sum = 0

while right < n:
    curr_sum += nums[right]

    while curr_sum >= s:
        count += n - right
        curr_sum -= nums[left]
        left += 1

    right += 1

print(count)
