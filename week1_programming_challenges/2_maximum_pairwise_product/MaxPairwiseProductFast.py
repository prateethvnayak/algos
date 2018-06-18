# Uses python3


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    # asser(len(a) == n)
    index1 = 0
    for i in range(1, n):
        if a[i] > a[index1]:
            index1 = i
    a[n - 1], a[index1] = swap(a[n - 1], a[index1])
    index2 = 1
    for i in range(1, n - 1):
        if a[i] > a[index2]:
            index2 = i
    a[n - 2], a[index2] = swap(a[n - 2], a[index2])
    result = a[n - 2] * a[n - 1]
    print(result)
