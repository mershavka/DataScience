import numpy as np
A = input()
B = input()
n = len(A) + 1
m = len(B) + 1
D = np.ones((n, m)) * np.inf
for i in range(n):
    D[i, 0] = i
for j in range(m):
    D[0, j] = j
for i in range(1, n):
    for j in range(1, m):
        c = int(A[i-1] != B[j-1])
        D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + c)
print(D[n-1,m-1])
    

