# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    val_unit = [float(val) / float(wght) for val, wght in zip(values, weights)]
    for i in range(len(weights)):
        if capacity == 0:
            return value
        valunit = max(val_unit)
        i = val_unit.index(valunit)
        val_unit[i] = -1
        a = min(weights[i], capacity)
        value += (a * valunit)
        weights[i] -= a
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
