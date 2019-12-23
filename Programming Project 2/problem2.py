import numpy as np


def bin_mult_and_xor(a, b):
    """
    Return mutliply a and b bit by bit and return the xor of all the bits.
    """
    a_binary = format(a, "b")
    b_binary = format(b, "b")
    max_bin_len = max(len(a_binary), len(b_binary))
    a_binary = format(a,"0" + str(max_bin_len) +"b")
    b_binary = format(b,"0" + str(max_bin_len) +"b")

    mult_and_xor = 0
    for i in range(max_bin_len):
        mult_and_xor ^= int(a_binary[i]) * int(b_binary[i])

    return mult_and_xor

def table_NL(s_box):
    """
    Compute the linear approximation table NL of the s_box.
    s_box is a permutation of its indexes.
    """
    n = len(s_box)
    table = np.zeros((n, n), dtype=int)

    for a in range(n):
        for b in range(n):
            nb_equal_0 = 0
            for x in range(n):
                # compute a xor x

                u = bin_mult_and_xor(a, x)
                #compute y=s_box[x] xor b
                v = bin_mult_and_xor(b, s_box[x])

                if u^v == 0:
                    nb_equal_0 +=1
            table[(a, b)] = nb_equal_0

    return table



s_box_test = [0xE, 0x4, 0xD, 0x1,
              0x2, 0xF, 0xB, 0x8,
              0x3, 0xA, 0x6, 0xC,
              0x5, 0x9, 0x0, 0x7]

#print(table_NL(s_box_test))

serpent_s3 = [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14]
NL = table_NL(serpent_s3)
print(NL)
bias_table = NL/16 - 1/2

print(bias_table)