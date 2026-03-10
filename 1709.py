def bubble_sort(arr, t):
    n = len(arr)
    ops = []

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ops.append((t, j + 1))  # +1 here

    return arr, ops


tc = int(input())

for _ in range(tc):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    operations = []

    arr1, ops = bubble_sort(arr1, 1)
    operations += ops

    arr2, ops = bubble_sort(arr2, 2)
    operations += ops

    for i in range(n):
        if arr1[i] > arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
            operations.append((3, i + 1))  # +1 here

    print(len(operations))
    for t, i in operations:
        print(t, i)
