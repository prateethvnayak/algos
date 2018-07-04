from fibonacci_huge import get_fibonacci_huge_naive
from fib_huge_fast import fib_fast, get_period
import random

while True:
    n = random.randint(1, 10000)
    m = random.randint(2, 1000)

    old = get_fibonacci_huge_naive(n, m)
    new = fib_fast(n, m)
    print(n, '\t', m, '\t')
    if old == new:
        print('OK\n')
    else:
        print('FAIL \n', old, '\t', new)
        break
