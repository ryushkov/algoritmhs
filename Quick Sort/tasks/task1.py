import random, time


def quicksort_median(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    mid1 = mid // 2
    mid2 = mid1 * 3

    first, middle1, middle, middle2, last = (
        arr[0],
        arr[mid1],
        arr[mid],
        arr[mid2],
        arr[-1],
    )
    pivot = sorted([first, middle1, middle, middle2, last])[2]

    left = []
    middle = []
    right = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    # Рекурсивно сортируем левую и правую части, объединяем все вместе
    return quicksort_median(left) + middle + quicksort_median(right)


start = time.time()
# arr = [random.randint(1, 1000000) for _ in range(1000000)]
# end = time.time()
# print(end - start)
arr = [64, 34, 25, 12, 22, 11, 90, 66, 98, 56, 43, 50]
sorted = quicksort_median(arr)
end = time.time()
print(end - start)
print(sorted)
