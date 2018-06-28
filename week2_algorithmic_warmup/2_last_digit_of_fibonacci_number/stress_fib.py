# Uses python 3
import numpy as np
from fibonnaci_last_digit_fast import fib_last_fast
from fibonacci_last_digit import get_fibonacci_last_digit_naive


while True:
    n = np.random.random_integers(0, 100)
    fst = fib_last_fast(n)
    old = get_fibonacci_last_digit_naive(n)

    print(n, '\t')
    if fst == old:
        print('OK \n')
    else:
        print('FAIL \n')
        print('output =', fst, '\t', 'actual =', old)
        break
