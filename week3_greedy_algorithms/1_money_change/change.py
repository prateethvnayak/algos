# Uses python3
import sys
from time import time


def get_change(m):
    # write your code here
    i = 0
    coin = [0, 0, 0]
    V = [10, 5, 1]
    # print(m, '\n')
    while m > 0:
        if min(m, V[i]) < m:
            m = m - V[i]
            coin[i] += 1
        elif V[i] == m:
            m = m - V[i]
            coin[i] += 1
            break
        else:
            i += 1

    return sum(coin)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    # s = time()
    print(get_change(m))
    # e = time()
    # print('\n ',(e - s))
