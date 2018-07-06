from sq_fast import fib_last_fast, squ_fast
from fibonacci_sum_squares import fibonacci_sum_squares_naive
import random

while True:
    n = random.randint(0, 100000)
    nv = fibonacci_sum_squares_naive(n)
    fst = squ_fast(n)
    print(n, '\t')
    if nv == fst:
        print('OK \n')
    else:
        print('FAIL \n %d \t %d'.format(nv, fst))
        break
