import numpy as np
import constants as const

def decode_section(section):
    log = []
    u1, u2 = np.split(section, 2)

    u2B = dot(u2, const.B)
    syndrome_1 = add(u1, u2B)
    log.append(f'Syndrome1 is {syndrome_1.astype(int)}')
    syndrome_1_weight = np.sum(syndrome_1)

    if syndrome_1_weight <= 3:
        u = np.append(syndrome_1, np.zeros(12).astype(int))
        log.append(f'Syndrome1 weight is {syndrome_1_weight}')
        log.append(f'u is equal {u.astype(int)}')
        return [log, add(section, u)]

    for idx, row in enumerate(const.B):
        sum = add(syndrome_1, row)
        sum_weight = np.sum(sum)

        if sum_weight <= 2:
            log.append(f'Syndrome1 and Brow[{idx}] sum weight <= 2 {sum.astype(int)}')
            e = np.zeros(12)
            e[idx] = 1
            u = np.append(sum, e)
            log.append(f'u equals {u.astype(int)}')
            return [log, add(section, u)]

    syndrome_2 = dot(syndrome_1, const.B)
    syndrome_2_weight = np.sum(syndrome_2)
    log.append(f'Syndrome2 is {syndrome_2.astype(int)}')

    if syndrome_2_weight <= 3:
        u = np.append(np.zeros(12).astype(int), syndrome_2)
        log.append(f'u equal {u.astype(int)}')
        return [log, add(section, u)]

    for idx, row in enumerate(const.B):
        sum = add(syndrome_2, row)
        sum_weight = np.sum(sum)
        if sum_weight <= 2:
            log.append(f'Syndrome2 and Brow[{idx}] is {sum.astype(int)}')
            e = np.zeros(12)
            e[idx] = 1
            u = np.append(e, sum)
            log.append(f'u equals {u.astype(int)}')
            return [log, add(section, u)]
    
    log.append('DECODING FAILED')
    return [log, []]

def decode(message):
    message = get_np_arr(message)
    result = []
    transmissions_required = 0
    for idx in range(0, len(message), 24):
        section = message[idx:idx + 24]
        decoded_result = decode_section(section)

        if(len(decoded_result) == 0):
            transmissions_required += 1
            result = np.append(result, message)

        result = np.append(result, decoded_result)

    return (result, transmissions_required)

def dot(a, b):
    return np.dot(a, b) % 2

def add(a, b):
    return np.add(a, b) % 2

def get_np_arr(array):
    if not isinstance(array, np.ndarray):
        array = np.array(array)

    return array 