"""В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i и b_i (a_i ≤b_i) — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит."""

from quick_sort import quick_sort
from binary_search import binary_search
from bisect import bisect_left, bisect_right

def main():
    n, _ = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dots = list(map(int, input().split()))
    result = []
    A_sorted = quick_sort(A, 0, len(A)-1)
    B_sorted = quick_sort(B, 0, len(B)-1)
    for dot in dots:
        N = bisect_right(A_sorted, dot)
        M = bisect_left(B_sorted, dot)
        result.append(N - M)
    print(*result)


if __name__ == "__main__":
    main()
