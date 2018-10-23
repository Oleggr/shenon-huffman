#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

text = '''The development of an information system, especially in the case where no automated data processing has previously existed, represents a marriage between two separate worlds. These worlds are those of the user community and of the system development team. The underlying organization of the user and developer communities, and the dissimilarities in their world views and languages, makes effective communication about software systems very difficult. User and developer worlds can vary in many dimensions. Each of these worlds has po- tentially very different conceptual frameworks, interests, and responsibilities. Users may be descriptive in their approach to problem solving while developers tend to be more analytical. Users may consider an information system to be only one of many, many things that interest them, while developers will tend to have as an over-riding priority the design and implemen- tation of the information system. Users may be torn by a variety of responsibilities, some of which keep them from participating effectively in information system development, despite their intentions or interest. The use of language by users and developers may also vary. For example, language may be used differently in the two worlds to indicate interest in or commitment to a project.'''

letters = -1
probability = 0

# Считаем количество символов

for line in text:
    letters += 1

# Считаем количество повторений конкретного символа

lettersArray = dict.fromkeys(text, 0) 
for c in text: 
    lettersArray[c] += 1 
 
# Выводим результат на экран
for c in dict.fromkeys(text, 0):
    probability = lettersArray[c] / (letters  * 1.0)
 
    print('\'' + str(c) + '\' --- ' 
        + str(lettersArray[c]) 
        + ' prob:' + str(math.ceil(probability*1000000)/1000000))

print('Всего букв:' + str(letters))
