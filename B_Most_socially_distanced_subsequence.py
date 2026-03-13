tc = int(input())
for _ in range(tc):
    n = int(input())
    perm = list(map(int, input().split()))
    
    left = 0
    right = 1
    endpoints = [perm[0]]
    increasing = perm[1] > perm[0]
    
    while right < n:
        if increasing:
            if perm[right] >= perm[right - 1]:
                right += 1
                continue
            else:
                
                endpoints.append(perm[right - 1])
                increasing = False
                left = right
                right += 1
        else:
            if perm[right] <= perm[right - 1]:
                right += 1
                continue
            else:
               
                endpoints.append(perm[right - 1])
                increasing = True
                left = right
                right += 1
    
    
    endpoints.append(perm[-1])
    
    print(len(endpoints))
    print(*endpoints)
