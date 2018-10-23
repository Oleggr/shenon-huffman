#! /usr/bin/env python
# -*- coding: utf-8 -*-

import operator

# Алфавит конкретного текста
# Хранит символ(ключ) и его количество повторений в тексте(значение)
alphabet = {}

# Вероятность появления символов из алфавита
# Хранит символ(ключ) и его вероятность(значение)
probability = {}

# Закодированный алфавит
# Хранит символ(ключ) и его код(значение)
alphabet_encoded = {}

# Лист со всеми символами
symbol = []

# Лист с вероятностями - зачем?)
prob = []

# Количество символов в тексте
count_of_symbols = 0

# Поиск кода для буквы
def search_code(zero_or_one_code, tmp_code, start_pos, end_pos, is_first):

    # Если это первое вхождение - очистить историю
    if is_first:
        full_code = ''
    else:
        full_code = tmp_code + zero_or_one_code

    # Если прошлись по всему списку, то выход
    if start_pos == end_pos:
        print('{} = {}'.format(symbol[start_pos], full_code))
        alphabet_encoded[symbol[start_pos]] = full_code
        return 0

    # Подсчет средней вероятности встречи символов
    average_prob = 0
    for i in range(start_pos, end_pos):
        average_prob += prob[i]
    average_prob /= 2

    # Считаем сумму вероятностей вхождения букв
    # и сравниваем со средней вероятностью для блока
    temp_summ_prob = 0
    index = start_pos
    while temp_summ_prob + prob[index] < average_prob \
            and index < end_pos:
        temp_summ_prob += prob[index]
        index += 1
        
    # Рекурсия для левой ветки
    search_code('0', full_code, start_pos, index, False)
    
    # Рекурсия для правой ветки
    search_code('1', full_code, index+1, end_pos, False)

# Определение алфавита текста и 
# вычисление количества повторений символа в тексте
with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        for i in line.lower():
            if i.isalnum():
                alphabet[i] = alphabet.get(i, 0) + 1
                count_of_symbols += 1

# Подсчет вероятности
for key in alphabet:
    probability[key] = alphabet[key] / count_of_symbols

# Сортировка вероятности по убыванию
probability_sorted = sorted(probability.items(), key=operator.itemgetter(1), reverse=True)

# Создание списков для упрощенной работы
for key, value in probability_sorted:
    # Создание списка символов
    symbol.append(key)
    # Создание списка вероятностей
    prob.append(value)
    print("{}: {:.8f}".format(key, value))

search_code(' ', ' ', 0, len(symbol)-1, True)

with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        for i in line.lower():
            if i.isalnum():
                print(alphabet_encoded.get(i, 0), end = ' ')
    print()
