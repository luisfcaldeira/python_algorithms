def merge(A: list, left: int, middle: int, right: int):
    n1: int = middle - left + 1
    n2: int = right - middle

    L: list = [0] * (n1)
    R: list = [0] * (n2)

    for i in range(0, n1):
        L[i] = A[left + i]

    for j in range(0, n2):
        R[j] = A[middle + j + 1]

    # L.insert(n1 + 1, float('inf'))
    # R.insert(n2 + 1, float('inf'))

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def mergeSort(A: list, left: int, right: int):
    if left < right: 
        middle: int = left + (right - left) // 2
        mergeSort(A, left, middle)
        mergeSort(A, middle + 1, right)
        merge(A, left, middle, right)


arr = [12, 11, 13, 5, 6, 7]
print(arr)
n = len(arr)

mergeSort(arr, 0, n-1)

print(arr)
