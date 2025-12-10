arr1 = [11, 12, 22, 25, 34, 43, 50, 56, 64, 66, 90, 98]
arr2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 67, 68, 69]
arr3 = []
i, j = 0, 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < len(arr1):
    arr3.append(arr1[i])
    i += 1

while j < len(arr2):
    arr3.append(arr2[j])
    j += 1

print(arr3)
