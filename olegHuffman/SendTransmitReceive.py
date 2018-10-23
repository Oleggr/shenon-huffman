from huff_1 import *

class Source():
    '''Класс источника данных'''

    _FILENAME = 'text.txt' 

    def __init__(self):
          pass

    def insert_message(self, user: str, message: str) -> None:
        self._user = user
        self._message = message

    def read_message_from_file(self, user):
        self._user = user
        temp_mess = ''

        with open(self._FILENAME, 'r', encoding='utf-8') as f:
            while True: 
                # prev_pos = f.tell()
                # temp_mess += f.readline()

                # next_pos = f.tell()
                # delta_pos = next_pos - prev_pos

                # f.seek(delta_pos, 1)
                # last_line_in_file = f.readline()
                
                last_line_in_file = f.readline()
                temp_mess += last_line_in_file

                if not last_line_in_file:
                    print('Текст из файла:\n' + temp_mess)
                    break

        self._message = temp_mess
                
    def encode_message(self) -> str:
        self._code = huffman_encode(self._message)
        self._encoded_message = "".join(self._code[ch] for ch in self._message)

    def send_message(self) -> str:
        return self._user, self._message

    def send_encoded_message(self) -> str:
        return self._user, self._encoded_message

    def send_encoded_alphabet(self):
        return self._code


class DataTransmissionChannel():
    '''Класс канала передачи данных'''

    def __init__(self):
        pass

    def get_message(self, user, message):
        self._user = user
        self._message = message

    def return_message(self):
        self._noise_adder()
        return self._user, self._message

    def _noise_adder(self):
        pass

    def count_symbols(self):
        pass

    def count_zeros(self):
        pass

    def count_ones(self):
        pass


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