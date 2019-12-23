from typing import List
import itertools

def binary_cartesian_product(nb_bits: int):
    """
    Compute binary possibilities of an nb_bits variable.
    """
    ranges = [range(0, 2) for i in range(nb_bits)]
    # In possibilities, we compute the nb_bits cartesian product of set([0, 1]}
    possibilities = list()
    for xs in itertools.product(*ranges):
        possibilities.append(tuple([*xs]))

    return possibilities


def x_generator(x_init, x_counter, x_list):
    """
        Generate x from the 3 first elements x1, x2, x3.
    """
    assert len(x_init) == 3

    while True:
        if x_counter < len(x_init):
            x_counter += 1
            yield x_list[x_counter - 1], x_counter, x_list
        else:
            x_list.append((x_list[x_counter - 3] + x_list[x_counter - 2]) % 2)
            x_counter += 1
            yield x_list[x_counter - 1], x_counter, x_list


def y_generator(y_init, y_counter, y_list):
    """
    Generate y from the 4 first elements y1, y2, y3, y4.
    """
    assert len(y_init) == 4
    while True:
        if y_counter < len(y_init):
            y_counter += 1
            yield y_list[y_counter - 1], y_counter, y_list
        else:
            y_list.append((y_list[y_counter - 4] + y_list[y_counter - 1]) % 2)
            y_counter += 1
            yield y_list[y_counter - 1], y_counter, y_list


def z_generator(z_init, z_counter, z_list):
    """
        Generate z from the 5 first elements z1, z2, z3, z4, z5.
    """
    assert len(z_init) == 5
    while True:
        if z_counter < len(z_init):
            z_counter += 1
            yield z_list[z_counter - 1], z_counter, z_list
        else:
            z_list.append((z_list[z_counter - 5] + z_list[z_counter - 3]) % 2)
            z_counter += 1
            yield z_list[z_counter - 1], z_counter, z_list


def generate_x_stream(initial, length):
    """
    Generate x stream of length length from initial state.
    """
    stream_list = list()
    counter = 0
    elt_list = list(initial)
    for i in range(length):
        res, counter, elt_list = x_generator(initial, counter, elt_list).__next__()
        stream_list.append(res)

    return stream_list

def generate_y_stream(initial, length):
    """
    Generate y stream of length length from initial state.
    """
    stream_list = list()
    counter = 0
    elt_list = list(initial)
    for i in range(length):
        res, counter, elt_list = y_generator(initial, counter, elt_list).__next__()
        stream_list.append(res)

    return stream_list


def generate_z_stream(initial, length):
    """
    Generate z stream of length length from initial state.
    """
    stream_list = list()
    counter = 0
    elt_list = list(initial)
    for i in range(length):
        res, counter, elt_list = z_generator(initial, counter, elt_list).__next__()
        stream_list.append(res)

    return stream_list

def compute_equality_percentage(stream1: List, stream2: List) -> float:
    """
    Compute percentage of stream1 and stream2 that match.
    """
    if len(stream1) != len(stream2):
        raise ValueError("stream1 and stream2 are of different lengths")

    nb_equal_values = 0
    for i in range(len(stream1)):  # both streams are of the same length
        if stream1[i] == stream2[i]:
            nb_equal_values += 1

    return nb_equal_values / len(stream1)


def compute_percentage_stream(stream, key_stream):
    """
    Computes the percentages of matches for each shift of the sequence.
    """
    percentage = list()
    percentage.append(compute_equality_percentage(stream, key_stream))

    return percentage


key_stream_str = '0000110011001001011101100010010'
key_stream_int = [int(elt) for elt in key_stream_str]
# For x, it was easy to find the sequence that repeated itself over and over,
# It is not so easy for the other variables
x_possibilities = binary_cartesian_product(3)
x_probabilities = list()
for x_possibility in x_possibilities:
     x_probabilities.append(compute_percentage_stream(generate_x_stream(x_possibility,
                                                                        len(key_stream_int)),
                                                      key_stream_int))

y_possibilities = binary_cartesian_product(4)
y_probabilities = list()
for y_possibility in y_possibilities:
     y_probabilities.append(compute_percentage_stream(generate_y_stream(y_possibility,
                                                                        len(key_stream_int)),
                                                      key_stream_int))


z_possibilities = binary_cartesian_product(5)
z_probabilities = list()
for z_possibility in z_possibilities:
     z_probabilities.append(compute_percentage_stream(generate_z_stream(z_possibility,
                                                                        len(key_stream_int)),
                                                      key_stream_int))

print([elt for elt in zip(x_possibilities, x_probabilities)])

print([elt for elt in zip(y_possibilities, y_probabilities)])

print([elt for elt in zip(z_possibilities, z_probabilities)])

select_x_init = [0, 1, 0]
possible_y_init = [[0, 0, 1, 0],
                   [0, 0, 1, 1],
                   [0, 1, 0, 1]]

possible_z_init = [[1, 0, 1, 0, 1],
                   [1, 1, 0, 0, 1]]

def compute_f(x, y, z):
    return (x*y + y*z + z) % 2

def generate_f_stream(x_init, y_init, z_init, length):
    x_stream = generate_x_stream(x_init, length)
    y_stream = generate_y_stream(y_init, length)
    z_stream = generate_z_stream(z_init, length)

    f_stream = [ compute_f(x_stream[i], y_stream[i], z_stream[i]) for i in range(length)]

    return f_stream

y_z_init_pairs = [[y, z] for y in possible_y_init for z in possible_z_init]

proba_dict = dict()
for y_init, z_init in y_z_init_pairs:
    f_stream = generate_f_stream(select_x_init, y_init, z_init, len(key_stream_int))
    proba_dict[(tuple(y_init), tuple(z_init))] = compute_percentage_stream(f_stream, key_stream_int)

print(proba_dict)

