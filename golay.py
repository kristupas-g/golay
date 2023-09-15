import encoding
import decoding
import channel

class Golay:
    def __init__(self, message, error_rate = 0):
        self.message = message

        padding_added, encoded_message = encoding.encode(message)
        self.padding_added = padding_added
        self.encoded_message = encoded_message

        self.noisy_message = channel.randomize(encoded_message, error_rate)

        decoded_message, transmissions_required = decoding.decode(self.noisy_message)
        self.decoded_message_with_padding = decoded_message
        self.decoded_message = decoded_message[:-padding_added]
        self.transmissions_required = transmissions_required
