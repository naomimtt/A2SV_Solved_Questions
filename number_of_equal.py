from collections import Counter
n, m = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
pairs = 0
c1 = Counter(arr1)
c2 = Counter(arr2)

for key in c1:
    pairs += c1[key] * c2.get(key, 0)
print(pairs)
