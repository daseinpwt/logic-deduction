# Find the solution for China's
# "2018 Criminal Investigation Reasoning Questions"
import itertools
import sys

A = 0
B = 1
C = 2
D = 3


def deduce(n, **dd):
    dd = [_v for _, _v in dd.items()]
    assert(sum(dd) == 1)
    assert(dd[v[n]])

occur = [None] * 4
for v in itertools.product(*([range(4)] * 10)):
    try:
        deduce(
            1,
            A=v[4] == C,
            B=v[4] == D,
            C=v[4] == A,
            D=v[4] == B)

        deduce(
            2,
            A=v[2] not in [v[5], v[1], v[3]],
            B=v[5] not in [v[2], v[1], v[3]],
            C=v[1] not in [v[2], v[5], v[3]],
            D=v[3] not in [v[2], v[5], v[1]])

        deduce(
            3,
            A=v[0] == v[4],
            B=v[1] == v[6],
            C=v[0] == v[8],
            D=v[5] == v[9])

        deduce(
            4,
            A=v[4] == v[7],
            B=v[4] == v[3],
            C=v[4] == v[8],
            D=v[4] == v[6])

        deduce(
            5,
            A=v[7] == v[1] == v[3],
            B=v[7] == v[0] == v[5],
            C=v[7] == v[2] == v[9],
            D=v[7] == v[4] == v[8])

        for i in range(4):
            occur[i] = 0
        for i in range(10):
            occur[v[i]] += 1
        assert(occur.count(min(occur)) == 1)
        deduce(
            6,
            A=occur[C] == min(occur),
            B=occur[B] == min(occur),
            C=occur[A] == min(occur),
            D=occur[D] == min(occur))

        deduce(
            7,
            A=abs(v[0] - v[6]) > 1,
            B=abs(v[0] - v[4]) > 1,
            C=abs(v[0] - v[1]) > 1,
            D=abs(v[0] - v[9]) > 1)

        deduce(
            8,
            A=(v[0] == v[5]) != (v[4] == v[5]),
            B=(v[0] == v[5]) != (v[4] == v[9]),
            C=(v[0] == v[5]) != (v[4] == v[1]),
            D=(v[0] == v[5]) != (v[4] == v[8]))

        diff = max(occur) - min(occur)
        deduce(
            9,
            A=diff == 3,
            B=diff == 2,
            C=diff == 4,
            D=diff == 1)

        print('Found an answer!')
        print("1-5: {}\n6-10: {}".format(
              [chr(v+ord('A')) for v in v[:5]],
              [chr(v+ord('A')) for v in v[5:]]))
        print("count:")
        print(occur)

    except AssertionError:
        continue
