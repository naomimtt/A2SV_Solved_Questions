tc = int(input())

for _ in range(tc):
    n = int(input())
    r = list(map(int, input().split()))
    
    m = int(input())
    b = list(map(int, input().split()))
    
    sum = 0
    best_r = 0
    for x in r:
        sum += x
        best_r = max(best_r, sum)
        
    sum = 0
    best_b = 0
    for x in b:
        sum += x
        best_b = max(best_b, sum)
        
    print(best_r + best_b)
