import random

def randomize(bit_array, error_rate):
    if error_rate > 1 or error_rate < 0:
        raise ValueError("loss_percentage must be between 1 and 0")
    error_rate = round(error_rate, 4)

    result = []
    for bit in bit_array:
        if random_chance() <= error_rate:
            bit = ~bit.astype(int) & 1 # This inverts the bit
        result += [bit]
    
    return result

def random_chance():
    chance = random.uniform(0,1)
    return round(chance, 4)

