import golay
import numpy as np
import random

def hamming_distance(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length")

    distance = 0

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            distance += 1

    return distance


def generate_random_arrays(num_arrays):
    random_arrays = []

    for _ in range(num_arrays):
        length = random.randint(1, 500)
        binary_array = np.random.randint(2, size=length)
        random_arrays.append(binary_array)

    return random_arrays

num_arrays = 10
error_rate = 0.05
messages = generate_random_arrays(num_arrays)

transmissions_required = 0
for idx, message in enumerate(messages):
    g = golay.Golay(message, error_rate)

    expected = g.message.astype(int)
    received = np.array(g.decoded_message).astype(int)
    if not np.array_equal(expected, received): 
        if g.transmissions_required > 0:
            transmissions_required += 1 
            continue

        print(f'Message no:{idx} failed out of {num_arrays} \n')
        print(f'Expected:\n{expected}')
        print(f'Received:\n{received}\n')
        print(f'Errors left {hamming_distance(expected, received)}')
        break

if transmissions_required != 0:
    print(f'{transmissions_required}/{num_arrays} messages had too many errors to fix')
