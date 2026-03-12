from collections import Counter

T = int(input())

for _ in range(T):
    s = input().strip()
    t = input().strip()

    cs = Counter(s)
    ct = Counter(t)

    if not cs <= ct:
        print("Impossible")
        continue

    # remove s letters from t
    for c in cs:
        ct[c] -= cs[c]

    # build sorted remaining characters
    rem = []
    for c in sorted(ct):
        rem.append(c * ct[c])
    rem = "".join(rem)

    # merge s with remaining characters
    i = j = 0
    ans = []

    while i < len(s) and j < len(rem):
        if s[i] <= rem[j]:
            ans.append(s[i])
            i += 1
        else:
            ans.append(rem[j])
            j += 1

    ans.append(s[i:])
    ans.append(rem[j:])

    print("".join(ans))
