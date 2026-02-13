t = int(input())
for _ in range(t):
    length = int(input())
    s = input()
 
    size = float('inf')
 
    if "aa" in s:
        size = min(size, 2)
    if "aba" in s or "aca" in s:
        size = min(size, 3)
    if "abca" in s or "acba" in s:
        size = min(size, 4)
    if "abbacca" in s or "accabba" in s:
        size = min(size, 7)
 
    print(size if size != float('inf') else -1)
