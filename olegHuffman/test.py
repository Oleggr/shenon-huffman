def remove_spaces(line):
    temp_list = line.split()
    new_line = ''

    for element in temp_list:
        new_line += element

    return new_line 

def counter_items_for_2_symbols(line):
    symbols_list = []
    return_list = []
    dict_counter = {}

    line = remove_spaces(line)

    if (len(line) % 2):
        line += 'Q'

    for i in range(0, len(line), 2):
        symbols_list.append(line[i] + line[i + 1])

    for symbol in symbols_list:
        dict_counter[symbol] = symbols_list.count(symbol)

    for key in dict_counter:
        val = dict_counter[key]
        temp_tuple = (key, val)
        return_list.append(temp_tuple)

    return return_list

counter_items_for_2_symbols('''test test testtest test \
test testetsese \
tset stt stets \
ste tste''')