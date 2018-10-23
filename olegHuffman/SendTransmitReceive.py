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

        with open(_FILENAME, 'r', encoding='utf-8') as f:
            while True:
                temp_mess = f.readline()
                if not temp_mess:
                    break

        self._message = temp_mess
                
    def encode_message(self) -> str:
        pass

    def send_message(self) -> str:
        return self._user, self._message

class Receiver():
    '''Класс приемника данных'''

    def __init__(self):
        pass 
        
    def get_message(self, user, message):
        self._user = user
        self._message = message

    def decode_message(self) -> str:
        pass

    def show_message(self) -> str:
        return self._user, self._message

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
