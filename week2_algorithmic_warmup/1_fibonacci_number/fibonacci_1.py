# Uses python3
import numpy as np


def fibonaci(n):
    if n <= 1:
        return n

    F = np.empty(shape=(n + 1))
    F[0] = 0
    F[1] = 1
    for i in range(2, len(F)):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]


n = int(input())
print(int(fibonaci(n)))
