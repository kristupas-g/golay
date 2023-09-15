import numpy as np
import constants as const

def decode(message):
    message = get_np_arr(message)
    result = []
    transmissions_required = 0
    for idx in range(0, len(message), 24):
        section = message[idx:idx + 24]
        u1, u2 = np.split(section, 2)

        u2B = dot(u2, const.B)
        syndrome_1 = add(u1, u2B)
        syndrome_1_weight = np.sum(syndrome_1)

        if syndrome_1_weight <= 3:
            u = np.append(syndrome_1, np.zeros(12).astype(int))
            result = np.append(result, add(section, u)[:-12])
            continue
        else:
            appended = False
            for idx, row in enumerate(const.B):
                sum = add(syndrome_1, row)
                sum_weight = np.sum(sum)

                if sum_weight <= 2:
                    e = np.zeros(12)
                    e[idx] = 1
                    u = np.append(sum, e)
                    result = np.append(result, add(section, u)[:-12])
                    appended = True
                    break

            if appended:
                continue

            syndrome_2 = dot(syndrome_1, const.B)
            syndrome_2_weight = np.sum(syndrome_2)

            if syndrome_2_weight <= 3:
                u = np.append(np.zeros(12).astype(int), syndrome_2)
                result = np.append(result, add(section, u)[:-12])
                continue

            for idx, row in enumerate(const.B):
                sum = add(syndrome_2, row)
                sum_weight = np.sum(sum)

                if sum_weight <= 2:
                    e = np.zeros(12)
                    e[idx] = 1
                    u = np.append(e, sum)
                    result = np.append(result, add(section, u)[:-12])
                    appended = True
                    break
            
            # Transmission required
            if not appended:
                transmissions_required += 1
                result = np.append(result, section[:-12])

    return (result, transmissions_required)

def dot(a, b):
    return np.dot(a, b) % 2

def add(a, b):
    return np.add(a, b) % 2

def get_np_arr(array):
    if not isinstance(array, np.ndarray):
        array = np.array(array)

    return array 