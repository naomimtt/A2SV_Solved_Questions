from collections import Counter
tc = int(input())
for _ in range(tc):
    n, k = map(int,input().split())
    colors = input()
    left = 0
    mini = Counter(colors[0:k])['W']
    curr = mini

    for right in range(len(colors)-k):
        if colors[right+k] == 'W':
            curr += 1
        if colors[right] == 'W':
            curr -= 1
            
        mini = min(mini, curr)
    print(mini)
