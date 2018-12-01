# from huffman_encode import *
# from huffman_encode_block import *
from huffman_encode_evenly import *
from noise_adder import *
from text_format import text_format

class Source():
    '''Класс источника данных'''

    _FILENAME = 'text.txt'

    def __init__(self):
        pass

    def insert_message(self, user: str, message: str) -> None:
        self._user = user
        self._message = text_format(message)

    def read_message_from_file(self, user):
        self._user = user
        temp_mess = ''

        with open(self._FILENAME, 'r', encoding='utf-8') as f:
            while True:

                last_line_in_file = f.readline()
                temp_mess += last_line_in_file

                if not last_line_in_file:
                    # print('Текст из файла:\n' + temp_mess)
                    break

        self._message = text_format(temp_mess)

    def encode_message(self) -> str:
        self._code = huffman_encode(self._message)
        self._encoded_message = \
                huffman_get_encode_message(self._code,self._message)

    def send_message(self):
        return self._user, self._message

    def send_encoded_message(self) -> str:
        return self._user, self._encoded_message

    def send_encoded_alphabet(self):
        return self._code

    def return_text_length(self):
        return len(self._message)

    def return_encoded_text_length(self):
        return len(self._encoded_message)

    def middle_count_of_symbols_per_letter(self):
        return round((len(self._encoded_message) / len(self._message)), 2)


class DataTransmissionChannel():
    '''Класс канала передачи данных'''

    def __init__(self):
        self._count_symbols = 0
        self._count_zeros = 0
        self._count_ones = 0

    def get_message(self, user, message):
        self._user = user
        self._message = message

    def return_clear_message(self):
        return self._user, self._message

    def return_noised_message(self):
        self._noised_message = noise_adder(self._message)
        # self._noised_message = noise_adder_random(self._message)
        return self._user, self._noised_message

    def count_symbols(self):
        for _ in self._message:
            self._count_symbols += 1
        return self._count_symbols

    def count_zeros(self):
        for i in self._message:
            if i == '0':
                self._count_zeros += 1
        return self._count_zeros

    def count_ones(self):
        for i in self._message:
            if i == '1':
                self._count_ones += 1
        return self._count_ones


class SecretDataTransmissionChannel():
    '''Класс секретного канала передачи данных'''
    '''Этот канал необходим для передачи закодированного алфавита'''

    def __init__(self):
        pass

    def get_secret_message(self, encoded_alphabet):
        self._code = encoded_alphabet

    def return_secret_message(self):
        return self._code


class Receiver():
    '''Класс приемника данных'''

    def __init__(self):
        pass

    def get_message(self, user, encoded_message):
        self._user = user
        self._encoded_message = encoded_message

    def get_encoded_alphabet(self, encoded_alphabet):
        self._code = encoded_alphabet

    def decode_message(self) -> str:
        self._message = huffman_decode(self._encoded_message, self._code)

    def show_message(self) -> str:
        return self._user, self._message

    def _show_encoded_message(self) -> str:
        return self._user, self._encoded_message

    def _show_encoded_alphabet(self) -> str:
        return self._code
