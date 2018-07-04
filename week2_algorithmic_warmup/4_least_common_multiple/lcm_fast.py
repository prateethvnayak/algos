# Uses python 3
import sys


def gcd_new(a, b):
    a_prime = a % b
    return gcd_new(b, a_prime)


def lcm_new(a, b):
    if b == 0 | a == 0:
        return 0
    gcd = gcd_new(a, b)
    return (a * b) // gcd


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_new(a, b))
