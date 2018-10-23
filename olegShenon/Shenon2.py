#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

# Выбор языка текста и алфавита en-0 ru-1

enOrRu = 0 

# Здесь задается анализируемый текст

#text = ['''The development of an information system, especially in the case where no automated data processing has previously existed, represents a marriage between two separate worlds. These worlds are those of the user community and of the system development team. The underlying organization of the user and developer communities, and the dissimilarities in their world views and languages, makes effective communication about software systems very difficult. User and developer worlds can vary in many dimensions. Each of these worlds has po- tentially very different conceptual frameworks, interests, and responsibilities. Users may be descriptive in their approach to problem solving while developers tend to be more analytical. Users may consider an information system to be only one of many, many things that interest them, while developers will tend to have as an over-riding priority the design and implemen- tation of the information system. Users may be torn by a variety of responsibilities, some of which keep them from participating effectively in information system development, despite their intentions or interest. The use of language by users and developers may also vary. For example, language may be used differently in the two worlds to indicate interest in or commitment to a project.''', 
#        '''Такому жанру как статья присуща шири практических обобщений, глубокий анализ фактов и явлений, четкая социальная направленность[источник не указан 3288 дней]. В статье автор рассматривает отдельные ситуации как часть более широкого явления. Автор аргументирует и выстраивает свою позицию через систему фактов. В статье выражается развернутая обстоятельная аргументированная концепция автора или редакции по поводу актуальной социологической проблемы. Также в статье журналист обязательно должен интерпретировать факты (это могут быть цифры, дополнительная информация, которая будет правильно расставлять акценты и ярко раскрывать суть вопроса).''']

text = ['tt pintin pint', '']

# Задается алфавит 

alphabet = ['abcdefghijklmnopqrstuvwxyz',
            'абвгдеёжзийклмнопрстуфхцчшщьыъэюя']
punctuationMarks = ' ,.:;!?/()-^$%@*\'\"'

# Здесь он выводится на экран

print('---Исходный текст---')
print(text[enOrRu])

# Объявление переменных-счетчиков

letters = 0
probability = 0

# Объявление списков для хранения алфавита
# и списков для обработанного алфавита
 
allLetters = []
countedAlphabet = []
sortedAlphabet = []

# Переводим текст в нижний регистр

textLow = text[enOrRu].lower()

# Считаем количество символов

for char in textLow:
    if char not in punctuationMarks:
        letters += 1
        allLetters.append(char)

# Определение ключа для сортировки

def byProbability_key(line):
    splitLine = line.split()
    return splitLine[2]

# Считаем сколько раз каждый символ 
# из алфавита попадается в тексте

for char in alphabet[enOrRu]:
    charCount = allLetters.count(char)
    # Вычисляем вероятность появления символа в тексте
    probability = charCount / (letters  * 1.0) 
    # Вывод в формате [символ] [кол-во появлений в тексте] [вер-ть]
    temp = str(char) + ' ' + str(charCount) + ' ' + str(math.ceil(probability*1000000)/1000000)
    countedAlphabet.append(temp)

sortedAlphabet = sorted(countedAlphabet, key = byProbability_key, reverse = True)

# Вывод на экран проанализированного и отсортированного алфавита

print('\n---Алфавит---')
for line in sortedAlphabet:
    print(line)

print('---')
print('Всего букв:' + str(letters))
