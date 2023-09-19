import decoding
import sys
import random
import numpy as np

def from_args():
    if len(sys.argv) < 2:
        return []
    values = sys.argv[1]
    numbers = values.split(',')
    numbers = np.array(numbers).astype(int)
    return numbers

def generate_random_binary_array(size=24):
    random_array = [random.choice([0, 1]) for _ in range(size)]
    return random_array

def pretty_print(arr):
    csv_string = ','.join(map(str, arr))
    print(csv_string)

def print_log(logs):
    for log in logs:
        print("\n")
        print(log)

vector = from_args()
if len(vector) == 0:
    vector = generate_random_binary_array() 
vector = np.array(vector)
pretty_print(vector)

log, decoded = decoding.decode_section(vector)
decoded= np.array(decoded).astype(int)

print(decoded)
print_log(log)
