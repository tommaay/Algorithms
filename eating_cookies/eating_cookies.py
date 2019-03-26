#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# n = 5
# 11111, 1211, 122, 131, 1121, 113, 1112
# 2111, 221, 23, 212,
# 311, 32

# n = 4
# 1111, 121, 13, 112
# 211, 22,
# 31

# n = 3
# 111, 12
# 21,
# 3

# n = 2
# 11
# 2

# n = 1
# 1


def eating_cookies(n, cache=None):
    if n < 2:
        return 1

    combos = [0 for i in range(n+1)]
    combos[0] = 1
    combos[1] = 1
    combos[2] = 2

    # as n increases by 1, combos will be the sum of the previous combos
    for i in range(3, n+1):
        combos[i] = combos[i - 3] + combos[i - 2] + combos[i - 1]
    print(combos)
    return combos[n]


print(eating_cookies(10))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
