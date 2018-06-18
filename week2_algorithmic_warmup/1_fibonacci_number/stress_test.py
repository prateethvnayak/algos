# Uses python3
import numpy as np


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonaci(n):
    F = np.empty(shape=(n+1))
    F[0] = 0
    F[1] = 1
    for i in xrange(2,len(F)):
        F[i] = F[i-1]+F[i-2]

    return int(F[n])

def stress_test():
    while True:
        n = np.random.randint(0,45)
        print(n)
        result_1 = fibonaci(n)
        result_2 = calc_fib(n)

        if result_1 == result_2:
            print('OK\n')
        else:
            print('Wrong Answer:', result_1,result_2)
            return

if __name__ =='__main__':
    stress_test()
