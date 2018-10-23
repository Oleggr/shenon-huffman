from SendTransmitReceive import *

a = Source()
aa = Source()

b = Receiver()

c = DataTransmissionChannel()

usr = input('User: ')
mes = input('Messg: ')

a.insert_message(usr,mes)
aa.read_message_from_file(usr)

# Отправляем по каналу сообщение из источника "a"

tmp_user_a = a.send_message()[0]
tmp_mess_a = a.send_message()[1]

c.get_message(tmp_user_a, tmp_mess_a)

tmp_user_a_1 = c.return_message()[0]
tmp_mess_a_1 = c.return_message()[1]

# Отправляем по каналу сообщение из источника "aa"

tmp_user_aa = aa.send_message()[0]
tmp_mess_aa = aa.send_message()[1]

c.get_message(tmp_user_aa, tmp_mess_aa)

tmp_user_aa_1 = c.return_message()[0]
tmp_mess_aa_1 = c.return_message()[1]

b.get_message(tmp_user_a_1, tmp_mess_a_1)
print(b.show_message())

b.get_message(tmp_user_aa_1, tmp_mess_aa_1)
print(b.show_message())