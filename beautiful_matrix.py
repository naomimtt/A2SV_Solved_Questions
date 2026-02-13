row = None
col = None
for i in range(5):
    numbers = list(map(int, input().split()))
    for j in range(5):
        if numbers[j] != 0:
            row = i
            col = j
print(abs(2-row) + abs(2-col))
