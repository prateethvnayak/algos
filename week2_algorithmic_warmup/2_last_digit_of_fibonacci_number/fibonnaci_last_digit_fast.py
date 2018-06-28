# Uses python3
import numpy as np
import sys


def fib_last_fast(n):
    if n <= 1:
        return n
    F = np.empty(shape=(n + 1))
    F[0] = 0
    F[1] = 1

    for i in range(2, len(F)):
        F[i] = (F[i - 1] + F[i - 2]) % 10

    return int(F[n])


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_fast(n))
