from statistics import median
import random

def partition(A, l, r):
    i = l
    x = A[round((r + l) / 2)]
    j = r
    while i < j:
        while A[i] < x:
            i += 1
        while x < A[j]:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return i,j


def quick_sort(A, l, r):
    if len(A) <= 1:
        return A
    if l < r:
        i, j = partition(A, l, r)
        quick_sort(A, l, j)
        quick_sort(A, i, r)
    return A

# lst = [random.randrange(1, 50000, 1) for _ in range(random.randrange(1, 50000, 1))]
# srt = quick_sort(lst, 0, len(lst) - 1)
# print(sorted(lst) == srt)