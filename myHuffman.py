from SendTransmitReceive import *

a = Source()
b = Receiver()

usr = input('User: ')
mes = input('Messg: ')
a.insert_message(usr,mes)

tmp_user = a.send_message()[0]
tmp_mess = a.send_message()[1]

b.get_message(tmp_user, tmp_mess)

print(b.show_message())