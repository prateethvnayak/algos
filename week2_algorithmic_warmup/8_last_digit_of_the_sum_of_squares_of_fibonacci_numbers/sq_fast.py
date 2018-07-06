# Uses python3
import sys


def fib_last_fast(n):
    if n <= 1:
        return n
    prev, curr = 1, 1
    for _ in range(n):
        prev, curr = curr % 10, (prev % 10 + curr % 10) % 10

    return (curr % 10), (prev % 10)


def squ_fast(n):
    if n <= 1:
        return n
    hor, ver = fib_last_fast(n)
    return int((ver * hor) % 10)
# Using the property that the sum of squares of n Fib numbers
# is the mul of nth Fib num and (n+1)th Fib num

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(squ_fast(n))
