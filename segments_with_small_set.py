n, k = map(int, input().split())
a = list(map(int, input().split()))

good = 0
left = 0
freq = {}

for right in range(n):
    freq[a[right]] = freq.get(a[right], 0) + 1

    while len(freq) > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        left += 1

    good += right - left + 1

print(good)
