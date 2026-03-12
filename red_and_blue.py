import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    s = 0
    best_r = 0
    for x in r:
        s += x
        best_r = max(best_r, s)
        
    s = 0
    best_b = 0
    for x in b:
        s += x
        best_b = max(best_b, s)
        
    print(best_r + best_b)
