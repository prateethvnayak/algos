# Uses python3
import sys


def fib_fast(n):
    n = (n + 2) % 60
    # print(n)

    if n == 0:
        return 9

    prev, curr = 0, 1

    for i in range(n - 1):
        # print(i)
        prev, curr = curr % 10, (prev % 10 + curr % 10) % 10
        # print(prev, curr, '\n')

    if curr == 0:
        return 9
    return curr % 10 - 1


def par_fast(m, n):
    if (m < 1):
        return fib_fast(n)
    else:
        s_n = fib_fast(n)
        s_m = fib_fast(m - 1)
        diff = (10 + s_n - s_m) % 10 if (s_n < s_m) else (s_n - s_m)
        return diff


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(par_fast(from_, to))

#############################################
 # if n <= 1:
 #        return n

 #    prev, curr = 0, 1

 #    for i in range(2, n + 3):
 #        prev, curr = curr, (prev + curr) % 10
 #        if i == (m + 1):
 #            s_m = 9 if (curr - 1) < 0 else (curr - 1)

 #    if m < 1:
 #        s_m = 0

 #    s_n = 9 if (curr - 1) < 0 else (curr - 1)
 #    diff = (10 + s_n - s_m) if (s_n < s_m) else (s_n - s_m)

###############################################
 # m_n, n_n = (m + 2) % 60, (n + 2) % 60
 #    if (m_n == n_n):
 #        m_n = m_n - 1
 #    prev, curr = 0, 1
 #    for i in range(n_n - 1):
 #        prev, curr = curr % 10, (prev % 10 + curr % 10) % 10
 #        if (i == m_n):
 #            if curr == 0:
 #                s_m = 9
 #            else:
 #                s_m = curr % 10 - 1
 #    if m == 0:
 #        s_m = 0

 #    s_n = 9 if (curr == 0) else (curr % 10 - 1)
 #    if n < 1:
 #        s_n = 0
 #    diff = (10 + s_n - s_m) % 10 if (s_n < s_m) else (s_n - s_m) % 10
 #    print('\n', s_n, '\t', s_m, '\n')
 #    if (m == n):
 #        return s_n
