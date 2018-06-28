import numpy as np
from lcm import lcm_naive
from lcm_fast import lcm_new
import time
while True:
    a = np.random.random_integers(0, 10000)
    b = np.random.random_integers(0, 10000)

    lcmold = lcm_naive(a, b)
    srt = time.time()
    lcmnew = lcm_new(a, b)
    end = time.time()
    print(a, '\t', b, '\t')
    if lcmold == lcmnew:
        print('OK \t', (end - srt), '\n')
    else:
        print('actual =', lcmold, '\touput =', lcmnew)
        print('\n FAIL')
        break
