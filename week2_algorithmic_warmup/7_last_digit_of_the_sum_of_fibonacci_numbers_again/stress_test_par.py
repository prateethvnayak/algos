# stress test
from fibonacci_partial_sum import fibonacci_partial_sum_naive
from partial_fast import par_fast
import random
while True:
    n = random.randint(0, 10000)
    m = random.randint(0, n)
    print(m, '\t', n, '\t')
    nav = fibonacci_partial_sum_naive(m, n)
    fst = par_fast(m, n)
    if nav == fst:
        print('OK \n')
    else:
        print('\n Fail\t', nav, '\t', fst)
        break
