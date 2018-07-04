# Stress Test
import random
import time

from fibonacci_sum_last_digit import fibonacci_sum_naive
from fib_lastsum_fast import fib_fast

while True:
    n = random.randint(0, 100000)
    strn = time.time()
    naive = fibonacci_sum_naive(n)
    endn = time.time()
    strf = time.time()
    fst = fib_fast(n)
    endf = time.time()

    print(n, '\t')
    if naive == fst:
        print('OK \n')
        # print('Naive time =', (endn - strn), '\t Fast time =', (endf - strf))
    else:
        print('\n Fail \t', naive, '\t', fst)
        break
