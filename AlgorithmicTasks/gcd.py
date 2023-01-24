# По данным двум числам 1 <= a, b <= 2*10^9 найдите их наибольший общий делитель

import time
from matplotlib import pyplot as plt

def timed(f, *args, n_iter=1000):
    print(*args)
    acc = float("inf")
    for _ in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)

    return acc

def compare(fs, *args):
    xs = list(range(len(args)))
    print(args)
    for f in fs:
        plt.plot(xs, [timed(f, chunk) for chunk in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)

def gcd3(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a > b:
        return gcd3(a % b, b)
    else:
        return gcd3(b % a, a)

def gcd4(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd4(b % a, a)

def main():
    compare([gcd3, gcd4], 14159572, 63967072)


if __name__ == "__main__":
    main()