from SendTransmitReceive import *

a = Source()
b = Receiver()
c = DataTransmissionChannel()

usr = input('User: ')
mes = input('Messg: ')

a.insert_message(usr,mes)

tmp_user = a.send_message()[0]
tmp_mess = a.send_message()[1]

c.get_message(tmp_user, tmp_mess)

tmp_user1 = c.return_message()[0]
tmp_mess1 = c.return_message()[1]

b.get_message(tmp_user1, tmp_mess1)

print(b.show_message())