# Найдите максимальный вес золота, который можно унести в рюкзаке (с повторениями)
# W - вместимость рюкзака
# n - число золотых слитков, weights/prices - веса и цены каждого слитка
def main_rep():
    W, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    assert(len(weights) == n)
    D = [0] * (W + 1)
    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                D[w] = max(D[w], D[w - weights[i]] + prices[i])
    print(D)

def main():
    import numpy as np
    W, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    assert(len(weights) == n)
    D = np.ones((W + 1, n + 1))
    for i in range(W + 1):
        D[i, 0] = 0
    for j in range(n + 1):
        D[0, j] = 0

    for w in range(1, W + 1):
        for i in range(1, n + 1):
            D[w, i] = D[w, i - 1]
            if weights[i - 1] <= w:
                D[w, i] = max(D[w, i], D[w - weights[i - 1], i - 1] + prices[i - 1])
    print(D)


if __name__ == "__main__":
    main()