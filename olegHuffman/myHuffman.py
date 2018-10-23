from SendTransmitReceive import *

transmitter = Source()
chanel = DataTransmissionChannel()
secret_chanel = SecretDataTransmissionChannel()
receiver = Receiver()

user = 'oleg'
message = 'test test test'

transmitter.insert_message(user, message)
transmitter.encode_message()

secret_chanel.get_secret_message(transmitter.send_encoded_alphabet())
receiver.get_encoded_alphabet(secret_chanel.return_secret_message())

chanel.get_message(
    transmitter.send_encoded_message()[0],
    transmitter.send_encoded_message()[1]
)

receiver.get_message(
    chanel.return_message()[0],
    chanel.return_message()[1]
)

receiver.decode_message()

print('передатчик закод. сообщ.: ', transmitter.send_encoded_message())
print('передатчик алфавит: ', transmitter.send_encoded_alphabet(), '\n')

print('канал закод. сообщ.: ', chanel.return_message(), '\n')

print('секр. канал алфавит:', secret_chanel.return_secret_message(), '\n')

print('приемник раскод. сообщ.: ', receiver.show_message())
print('приемник закод. сообщ.: ', receiver._show_encoded_message())
print('приемник алфавит: ', receiver._show_encoded_alphabet(), '\n')