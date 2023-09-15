import numpy as np
import constants

def encode(bit_array):
    padding_length, message = add_padding(bit_array)
    encoded_message = np.array([])
    for idx in range(0,len(message), 12):
        section = message[idx:idx + 12]
        encoded_section = np.dot(section, constants.generator_matrix) % 2
        encoded_message = np.append(encoded_message, encoded_section)
    return (padding_length, encoded_message)
    
def add_padding(bit_array): # this is needed because the message needs to a multiple of 12
    padding_length = (24 - len(bit_array) % 24) % 24
    padded_message = np.concatenate((bit_array, np.zeros(padding_length)))
    return (padding_length, padded_message)