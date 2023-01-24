'''По данному числу 1≤n≤10^9 найдите максимальное число k, 
для которого n можно представить как сумму k различных натуральных слагаемых. 
Выведите в первой строке число k, во второй — k слагаемых.'''


def main():
    n = int(input())
    result = []
    tmp = 0
    while n:
        tmp += 1
        if n - tmp and n - tmp <= tmp:
            continue
        result.append(tmp)
        n -= tmp
    print(len(result))
    print(*result)

if __name__ == "__main__":
    main()
