"""У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
заменить x на 2x, 3x или x+1. По данному целому числу 1≤n≤10^5 определите минимальное число операций k,
необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел."""
from math import inf
# Рекурсивный алгоритм
def calc(steps):
    steps = [steps]
    value = steps[-1]
    if value == 1:
        return steps
    a = b = c = inf
    if value % 3 == 0:
        a_l = calc(steps + [value // 3])
        a = len(a_l)
    if value % 2 == 0:
        b_l = calc(steps + [value // 2])
        b = len(b_l)
    c_l = calc(steps + [value - 1])
    c = len(c_l)
    m = min(a, b, c)
    if a == m:
        steps = a_l
    elif b == m:
        steps = b_l
    else:
        steps = c_l
    return steps

def main():
    n = int(input())
    steps = calc(n)
    print(len(steps) - 1)
    print(*reversed(steps))
    return

# Оптимальность для подзадачи: префикс в оптимальной последовательности операций тоже оптимален (метод вырезать и вставить)
# То есть 

def calc(n):
    if n == 1:
        return [1]
    D = [0, 1, 1, 1] + [inf] * (n - 3)

    for i in range(1, n+1):
        for j in (i + 1, i * 2, i * 3):
            if D[j] + 1 < D[i]:
                D[i] = 1 + D[j]

    for i in range(4, n + 1):
        if i % 3 == 0:
            j = i // 3
            if D[j] + 1 < D[i]:
                D[i] = 1 + D[j]
        if i % 2 == 0:
            j = i // 2
            if D[j] + 1 < D[i]:
                D[i] = 1 + D[j]
        if i - 1 > 0:
            j = i - 1
            if D[j] + 1 < D[i]:
                D[i] = 1 + D[j]
    A = [n]
    i = n
    while i > 3:
        for j in range(i - 1, -1, -1):
            if D[j] == D[i] - 1 and (i / 2 == j or i / 3 == j or i - 1 == j):
                A.append(j)
                i = j
                break
    A.append(1)
    return A

if __name__ == "__main__":
    main()