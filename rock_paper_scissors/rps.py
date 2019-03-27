#!/usr/bin/python

import sys

# n=1 - 3 combinations
# n=2 - 9 combintions
# n=3 - 27 combinations

# the number of combinations is the result of 3**n


def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    if n == 0:
        return [[]]

    combos = []
    temp = ['rock', 'paper', 'scissors']

    if n == 1:
        return [[combo] for combo in temp]

    for idx in range(2, n+1):
        combos = temp
        temp = []
        for o in options:
            for li in combos:
                if isinstance(li, list):
                    combo = [o] + li
                elif isinstance(li, str):
                    combo = [o] + [li]
                temp.append(combo)
        combos = temp
    return(combos)


print(rock_paper_scissors(3))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays=int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
