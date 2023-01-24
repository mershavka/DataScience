from math import inf
def main():
    n = int(input())
    weights = list(map(int, input().split()))

    max_sum = [0] + n * [-inf]
    for i in range(1, n + 1):
        max_sum[i] = max(max_sum[i - 2], max_sum[i - 1]) + weights[i - 1]

    print(max_sum[-1])

def main():
    input()
    curr = prev = 0
    for s in input().split():
        prev, curr = curr, max(curr,prev)+int(s)
    print(curr)

if __name__ == "__main__":
    main()