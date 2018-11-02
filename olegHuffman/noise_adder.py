from random import randint

# Функция добавления шума в строку двоичных символов
def noise_adder(message, noise_percent = 10):

    # Здесь вычисляется количествосимволов, которое 
    # должно быть заменено, соответственно проценту шума
    noise_amount = round((noise_percent * len(message)) / 100)

    # Массив номеров уже измененных символов
    already_changed = []

    for i in range(0, noise_amount):

        while True:

            # Вычисление номера символа для замены
            random_number = randint(0, len(message) - 1)

            # Если символ с этим номером не менялся,
            # производим замену
            if random_number not in already_changed:
                already_changed.append(random_number)

                # Меняем символ на другой
                # была 1 ставим 0
                #  был 0 ставим 1
                if message[random_number] == '1':
                    message = message[:random_number] \
                            + '0' + message[random_number + 1:]
                else:
                    message = message[:random_number] \
                            + '1' + message[random_number + 1:]
                break

    return message