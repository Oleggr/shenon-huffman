# Модуль для работы с мин. кучей из стандартной библиотеки Python
import heapq

# Словарь в котором для каждого объекта поддерживается счетчик
from collections import Counter
from collections import namedtuple

# Добавим классы для хранения информации о структуре дерева
# Воспользуемся функцией namedtuple из стандартной библиотеки

# Класс для ветвей дерева - внутренних узлов. У них есть потомки
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        # Чтобы обойти дерево нам нужно:

        # Пойти в левого потомка, добавив к префиксу '0'
        self.left.walk(code, acc + '0')

        # Затем пойти в правого потомка, добавив к префиксу '1'
        self.right.walk(code, acc + '1')

# Класс для листьев дерева, у него нет потомков, но есть значение символа
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        # Потомков у листа нет, по этому для значения мы запишем построенный код для данного символа

        # Если строка длиной 1 то acc = '', для этого случая установим значение acc = '0'
        code[self.char] = acc or '0'

# функция кодирования строки в коды Хаффмана
def huffman_encode(s):
    # Инициализируем очередь с приоритетами
    h = []

    # Построим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
    for ch, freq in counter_items_for_2_symbols(s):
        print(ch, freq, counter_items_for_2_symbols(s))
        print()
        # Очередь будет представлена частотой символа, счетчиком и самим символом
        h.append((freq, len(h), Leaf(ch)))

    # Построим очередь с приоритетами
    heapq.heapify(h)
    # Инициализируем значение счетчика длиной очереди
    count = len(h)

    # Пока в очереди есть хотя бы 2 элемента
    while len(h) > 1:

        # Вытащим элемент с минимальной частотой - левый узел
        freq1, _count1, left = heapq.heappop(h)
        # Вытащим следующий элемент с минимальной частотой - правый узел
        freq2, _count2, right = heapq.heappop(h)

        # Поместим в очередь новый элемент, у которого частота 
        # равна сумме частот вытащенных элементов

        # Добавим новый внутренний узел у которого
        # Потомки left и right соответственно
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        # Инкрементируем значение счетчика при добавлении нового элемента дерева
        count += 1

    # Инициализируем словарь кодов символов
    code = {}

    # Если строка пустая, то очередь будет пустая и обходить нечего
    if h:
        # В очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        [(_freq, _count, root)] = h

        # Обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
        root.walk(code, '')
    print(code)
    # Возвращаем словарь символов и соответствующих им кодов
    return code

# Функция декодирования исходной строки по кодам Хаффмана
def huffman_decode(encoded, code):
    # Инициализируем массив символов раскодированной строки
    sx = []
    # Инициализируем значение закодированного символа
    enc_ch = ''
    # Обойдем закодированную строку по символам
    for ch in encoded:
        # Добавим текущий символ к строке закодированного символа
        enc_ch += ch
        # Постараемся найти закодированный символ в словаре кодов
        for dec_ch in code:

            # Если закодированный символ найден,
            if code.get(dec_ch) == enc_ch:
                # Добавим значение раскодированного символа к массиву раскодированной строки
                sx.append(dec_ch)
                # Обнулим значение закодированного символа
                enc_ch = ''
                break
    # Вернем значение раскодированной строки
    return ''.join(sx)


def huffman_get_encode_message(code, message):

    return_str = ''
    temp_str = ''
    temp_code = ''

    for i in range(0, len(message), 1):
        temp_str = message[i]

        for key in code:
            if key == temp_str:
                temp_code = code[key]
                break

        return_str += temp_code

    return return_str#"".join(code[symbol] for symbol in message)


def counter_items_for_2_symbols(line):
    symbols_list = []
    return_list = []
    dict_counter = {}

    # line = remove_spaces(line)

    if (len(line) % 2):
        line += 'Q'

    for i in range(0, len(line), 1):
        symbols_list.append(line[i])

    for symbol in symbols_list:
        dict_counter[symbol] = 1

    for key in dict_counter:
        val = dict_counter[key]
        temp_tuple = (key, val)
        return_list.append(temp_tuple)

    return return_list