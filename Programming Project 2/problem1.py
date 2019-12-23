import numpy as np

"""
This is the solution for problem one of programming porject 2.
The problem is defined in the 4th edition Cryptography Theory and Practice
by Stinson and Paterson under problem 4.16.
For this whole problem we consider that the s-boxes are bijective.
"""


# Question a

def delta_set(x_prime, m):
    """
    Returns the set of all the ordered pairs having an input x-or equal
    to x_prime. It is the set of the ordered pairs (x, x_prime + x) modulo 2.
    m is the number of elements of the substitution box.
    """
    delta = set()
    for x in range(m):
        delta.add((x, x ^ x_prime))

    return delta


def table_ND(s_box):
    """
    Compute the difference distribution table ND of the s_box.
    s_box is a permutation of its indexes.
    """
    m = len(s_box)
    table = np.zeros((m, m), dtype=int)
    for x_prime in range(m):
        delta = delta_set(x_prime, m)
        for x, x_star in delta:
            y_prime = s_box[x] ^ s_box[x_star]
            table[x_prime][y_prime] += 1

    return table


s_box = [0xE, 0x2, 0x1, 0x3,
         0xD, 0x9, 0x0, 0x6,
         0xF, 0x4, 0x5, 0xA,
         0x8, 0xC, 0x7, 0xB]

serpent_s3 = [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14]
print(table_ND(serpent_s3)/16)
# Question b
