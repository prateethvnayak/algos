# Uses python 3
from gcd import gcd_naive
from gcd_fast import gcd_new
import numpy as np

while True:
    a = np.random.random_integers(1, 1000)
    b = np.random.random_integers(1, 1000)
    print(a, '\t', b, '\n')
    gcd_old = gcd_naive(a, b)
    gcd_n = gcd_new(a, b)

    if gcd_old == gcd_n:
        print('OK')
    else:
        print('FAILED')
        break
