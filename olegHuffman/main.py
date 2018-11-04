from huffman_classes import *
# import pdb; pdb.set_trace() 

# Передатчик
transmitter = Source()

# Канал связи для передачи сообщения
# и серетный канал связи для передачи алфавита
chanel = DataTransmissionChannel()
secret_chanel = SecretDataTransmissionChannel()

# Приемник неизмененного сигнала иизмененного соответственно
receiver_clear = Receiver()
receiver_noised = Receiver()

# Исходные данные
user = 'oleg'
message = 'test test \ntesttest tes.,/t tt'
print(message)

# Получение сообщение передатчиком 
# и шифрование этого сообщения
transmitter.insert_message(user, message)
transmitter.encode_message()

# Передача через секретный канал связи 
# шифрованного алфавита на приемник
secret_chanel.get_secret_message(transmitter.send_encoded_alphabet())
receiver_noised.get_encoded_alphabet(secret_chanel.return_secret_message())
receiver_clear.get_encoded_alphabet(secret_chanel.return_secret_message())

# Передача сообщения в канал связи
chanel.get_message(
    transmitter.send_encoded_message()[0],
    transmitter.send_encoded_message()[1]
)

# Получение приемником из канала связи сообщения без помех
receiver_clear.get_message(
    user,
    chanel.return_clear_message()[1]
)

# Декодирование шифрованного неизмененного сообщения
receiver_clear.decode_message()

# Получение приемником из канала связи сообщения с помехами
receiver_noised.get_message(
    user,
    chanel.return_noised_message()[1]
)

# Декодирование шифрованного измененного сообщения
receiver_noised.decode_message()

# Вывод на экран результатов работы программы на каждом шаге
print()
print('\x1b[1;30mпередатчик \x1b[0mсообщ.:', transmitter.send_message())
print('\x1b[1;30mпередатчик \x1b[0mзакод. сообщ.:', transmitter.send_encoded_message())
print('\x1b[1;30mпередатчик \x1b[0mалфавит:', transmitter.send_encoded_alphabet())
print()
print('\x1b[1;30mканал \x1b[0mзакод. сообщ.:', chanel.return_clear_message())
print('\x1b[1;30mканал \x1b[0mΣ символов:', chanel.count_symbols())
print('\x1b[1;30mканал \x1b[0mΣ 0:', chanel.count_zeros())
print('\x1b[1;30mканал \x1b[0mΣ 1:', chanel.count_ones())
print()
print('\x1b[1;30mсекр.канал \x1b[0mалфавит:', secret_chanel.return_secret_message())
print()
print('\x1b[1;30mприемник \x1b[0mраскод. сообщ.:', receiver_clear.show_message())
print('\x1b[1;30mприемник \x1b[0mзакод. сообщ.:', receiver_clear._show_encoded_message())
print('\x1b[1;30mприемник \x1b[0mалфавит:', receiver_clear._show_encoded_alphabet())
print('\x1b[1;30mприем. с помехами \x1b[0mраскод. сообщ.:', receiver_noised.show_message())
print('\x1b[1;30mприем. с помехами \x1b[0mзакод. сообщ.:', receiver_noised._show_encoded_message())
print()
print('\x1b[1;30mЕще раз, для сравнения:')
print('\x1b[1;30mпередатчик \x1b[0mсообщ.:', '\t\t\t', transmitter.send_message())
print('\x1b[1;30mприем. с помехами \x1b[0mраскод. сообщ.:', '\t', receiver_noised.show_message())
print('\x1b[1;30mпередатчик \x1b[0mзакод. сообщ.:', '\t', transmitter.send_encoded_message())
print('\x1b[1;30mприем. с помехами \x1b[0mзакод. сообщ.:', receiver_noised._show_encoded_message())
print()