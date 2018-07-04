# Uses python3
import sys


def par_fast(m, n):
    if n <= 1:
        return n

    prev, curr = 0, 1

    for i in range(2, n + 3):
        prev, curr = curr, (prev + curr) % 10
        if i == (m + 1):
            s_m = 9 if (curr - 1) < 0 else (curr - 1)

    if m < 1:
        s_m = 0

    s_n = 9 if (curr - 1) < 0 else (curr - 1)
    diff = (10 + s_n - s_m) if (s_n < s_m) else (s_n - s_m)

    return diff


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(par_fast(from_, to))
