tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    casino = []
    for i in range(n):
        casino.append(list(map(int, input().split())))
    casino.sort(key = lambda x : x[-1])
    for c in casino:
        if c[0]<= k <= c[1]:
            k = max(k, c[2])
    print(k)

