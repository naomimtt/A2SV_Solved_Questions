tc = int(input())

for _ in range(tc):
    n = int(input())
    a, b = list(input()), input()

    valid = set()
    flip = 0
    flipped = False

    for i in range(n):
        if a[i] == '0':
            flip -= 1
        else:
            flip += 1
        if flip == 0:
            valid.add(i)
    
    for i in range(n-1, -1, -1):
        if flipped:
            if a[i] == '0':
                temp = '1'
            else:
                temp = '0'
        else:
            temp = a[i]
        if temp == b[i]:
            continue
        else:
            if i in valid:
                flipped = not flipped
            else:
                print('NO')
                break
    else:

        print('YES')
