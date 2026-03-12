tc = int(input())
for _ in range(tc):
    s = input().strip()
    
    i = 0
    
    if len(s) == 1:
        print(s)
        continue
    working = []
    while  i <= len(s) - 1:
        if i == len(s) - 1:
            working.append(s[i])
            i += 1
        elif s[i] == s[i+1]:
            i += 2
            
        else:
            working.append(s[i])
            i += 1
    working = set(working)
    print(''.join(sorted(working)))
