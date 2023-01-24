def fib(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = (b, a + b)
    return b

def fib_last_digit(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = (b, (a + b) % 10)
    return b

def fib_mod(n, m):
    if m <= 1:
        return 0
    a, b = 0, 1
    fi_mod_m = [a, b]
    period = 1
    for i in range(2, m*6+1):
        rem = ((a % m) + (b % m)) % m
        period = i - 2
        fi_mod_m.append(rem)
        if period > 2 and b == 1 and a == 0:
            period = i - 2
            break
        a, b = (b, rem)
    print(period)
    result = fi_mod_m[n % period]
    print(fi_mod_m)
    return result

def main():
    n, m = map(int, input("Enter two digits:\n").split())
    print("N fibonachi: ", fib(n))
    print("M: ", m)
    print("N mod M: ", fib_mod(n, m))

if __name__ == "__main__":
    main()