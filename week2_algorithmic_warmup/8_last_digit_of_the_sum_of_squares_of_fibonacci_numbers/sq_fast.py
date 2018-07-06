# Uses python3
from sys import stdin
# import numpy


def fib_last_fast(n):
    if n <= 1:
        return n
    # F = np.empty(shape=(n + 1))
    prev, curr = 0, 1
    # F[1] = 1
    for i in range(n - 1):
        prev, curr = curr % 10, (prev % 10 + curr % 10) % 10

    return curr % 10


def squ_fast(n):
    if n < 1:
        return 0
    else:
        ver = fib_last_fast(n)
        hor = fib_last_fast(n + 1)
        return (ver * hor) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(squ_fast(n))
