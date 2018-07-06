# Uses python3
import sys


def fib_fast(n):
    n = (n + 2) % 60
    # print(n)

    if n == 0:
        return 9

    prev, curr = 0, 1

    for i in range(n - 1):
        print(i)
        prev, curr = curr % 10, (prev % 10 + curr % 10) % 10
        print(prev, curr, '\n')

    if curr == 0:
        return 9
    return curr % 10 - 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    print(fib_fast(6))
