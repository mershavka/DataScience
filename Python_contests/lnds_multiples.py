"""Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9.
Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1 ≤ i_1 < i_2 <...< i_k ≤ n,
в которой каждый элемент делится на предыдущий."""

# Решение за O(n^2)

def main_n2():
    n = int(input())
    A = list(map(int, input().split()))
    D = [0] * n
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if (A[j] >= A[i]) and (D[i] < D[j] + 1):
                D[i] = D[j] + 1
    max_len = max(D)
    print(max_len)
    ind_max = D.index(max_len)
    import queue
    q = queue.LifoQueue()
    q.put(ind_max + 1)
    for i in (range(ind_max, -1, -1)):
        if D[i] == D[ind_max] - 1 and A[ind_max] <= A[i]:
            q.put(i + 1)
            ind_max = i
    while not q.empty():
        print(q.get(), end=' ')

def right_binary_search(value, sorted_list):
    # l <= x < r
    left = -1
    right = len(sorted_list)
    while right - left > 1:
        mean = (left + right)//2
        if sorted_list[mean] <= value:
            left = mean
        else:
            right = mean
    if sorted_list[left] == value:
        return left
    return right
# Решение за O(nlogn)     

def main_nlogn():
    n = int(input())
    A = list(map(int, input().split()))
    from math import inf
    # D - список из наименьших последних элементов во всех возрастающих последовательностях c длинами,
    # равными соответствующему индексу i. С ростом i не убывает d[i]
    D = [-inf] + [inf] * n
    # pos[i] - индекс d[i] в массиве A
    pos = [-1] * (n + 1)
    # pos[i] - индекс элемента в массиве A, который предшествовал A[i] в НВП
    prev = [-1] * (n + 1)
    
    from math import inf
    
    for i in range(n):
        bin_key = A[i]
        r = right_binary_search(bin_key, D)
        if bin_key < D[r]:
            D[r] = bin_key
            pos[r] = i
            prev[i] = pos[r-1]
            max_len = r
    print(max_len)
    ans = [0]*max_len

    pred_ind = pos[max_len]
    ans[-1] = pred_ind
    k = -2
    while pred_ind > 0:
        pred_ind = prev[pred_ind]
        ans[k] = pred_ind
        k -= 1
    print(*ans)

if __name__ == "__main__":
    main_n2()