import random
from collections import deque

def inversions(data):
    # data = [random.randrange(1, 20, 1) for _ in range(random.randrange(1, 20, 1))]
    queue = deque(data)
    if len(queue) <= 1:
        return 0

    inversions = 0
    joined_pairs = []
    while len(queue) > 1:
        left = queue.popleft()
        right = queue.popleft()
        if len(queue) == 1:
            last = queue.pop()
            inversions += [(left <= right), (right <= last), (left <= last)].count(False)
            joined_pairs.append(sorted([left, right, last]))
            break
        if left > right:
            inversions += 1
            left, right = right, left
        joined_pairs.append([left, right])

    final_joined = []
    joined_pairs = deque(joined_pairs)

    final_joined = joined_pairs.copy()
    while len(final_joined) > 1:
        final_joined.clear()
        while len(joined_pairs) > 1:
            joined = []
            l_p = deque(joined_pairs.popleft())
            r_p = deque(joined_pairs.popleft())
            while l_p and r_p:
                l = l_p.popleft()
                r = r_p.popleft()
                if l <= r:
                    joined.append(l)
                    r_p.appendleft(r)

                else:
                    l_p.appendleft(l)
                    inversions += len(l_p)
                    joined.append(r)
            if len(r_p) > 0:
                joined.extend(list(r_p))
            if len(l_p) > 0:
                joined.extend(list(l_p))
            final_joined.append(list(joined))
        if len(joined_pairs) == 1:
            final_joined.extend(joined_pairs)
        
        joined_pairs.clear()
        joined_pairs = final_joined.copy()

    return inversions

# def main():
#     n = int(input())
#     A = map(int, input().split())
#     print(inversions(A))

def main():
    n = 6
    A = [10, 8, 6, 2, 4, 5]
    print(inversions(A))

if __name__ == "__main__":
    main()