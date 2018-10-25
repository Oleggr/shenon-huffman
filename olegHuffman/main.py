from HuffmanClasses import *

transmitter = Source()

chanel = DataTransmissionChannel()
secret_chanel = SecretDataTransmissionChannel()

receiver_clear = Receiver()
receiver_noised = Receiver()

user = 'oleg'
message = 'test test testtt'

transmitter.insert_message(user, message)
transmitter.encode_message()

secret_chanel.get_secret_message(transmitter.send_encoded_alphabet())
receiver_noised.get_encoded_alphabet(secret_chanel.return_secret_message())
receiver_clear.get_encoded_alphabet(secret_chanel.return_secret_message())

chanel.get_message(
    transmitter.send_message()[0],
    transmitter.send_message()[1]
)

# Передача сообщения по каналу без помех

receiver_clear.get_message(
    user,
    chanel.return_clear_message()[1]
)

receiver_clear.decode_message()

# Передача сообщения по каналу с помехами

receiver_noised.get_message(
    user,
    chanel.return_noised_message()[1]
)

receiver_noised.decode_message()

print()
print('\x1b[1;30mпередатчик \x1b[0mзакод. сообщ.:', transmitter.send_message())
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

print('\x1b[1;30mприем. с помехами \x1b[0mраскод. сообщ.:', receiver_noised.show_message())
print('\x1b[1;30mприем. с помехами \x1b[0mзакод. сообщ.:', receiver_noised._show_encoded_message())

print('\x1b[1;30mприемник \x1b[0mалфавит:', receiver_clear._show_encoded_alphabet())
print()