from collections import Counter

tc = int(input())

for _ in range(tc):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    cost = 0
    left_socks = Counter(socks[:l])
    right_socks = Counter(socks[l:])

    for sock in left_socks:
        if sock in right_socks:
            pairs = min(left_socks[sock], right_socks[sock])
            l -= pairs
            r -= pairs
            left_socks[sock] -= pairs
            right_socks[sock] -= pairs

    if r > l:
        heavy = right_socks
    else:
        heavy = left_socks

    flips = 0
    req = abs((l - r) // 2)
    for sock in heavy:
        if flips == req:
            break
        if heavy[sock] >= 2:
            available = heavy[sock] // 2
            flipp = min(available, req - flips)
            cost += flipp
            flips += flipp
            heavy[sock] -= flipp * 2

    for sock in heavy:
        if heavy[sock] != 0:
            cost += heavy[sock]

    print(cost)
