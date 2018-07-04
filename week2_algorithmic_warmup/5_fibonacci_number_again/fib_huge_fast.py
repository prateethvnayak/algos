# Uses python3
import sys


def get_period(m):
    a, b = 0, 1
    c = a + b
    for i in range(0, m * m):
        c = (a + b) % m
        a, b = b, c
        if(a == 0 and b == 1):
            return i + 1


def fib_fast(n, m):
    per = get_period(m)
    res = n % per
    prev, curr = 0, 1
    for i in range(1, res):
        res = (prev + curr) % m
        prev, curr = curr, res
    return res % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fib_fast(n, m))
