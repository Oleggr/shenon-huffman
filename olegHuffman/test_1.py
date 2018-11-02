from collections import Counter

def counter_items_for_2_symbols(line):
    symbols_list = []
    return_list = []
    dict_counter = {}

    #line = remove_spaces(line)

    if (len(line) % 2):
        line += 'Q'

    # for i in range(0, len(line), 2):
    #     symbols_list.append(line[i] + line[i + 1])

    for i in range(0, len(line)):
        symbols_list.append(line[i])

    for symbol in symbols_list:
        dict_counter[symbol] = symbols_list.count(symbol)

    for key in dict_counter:
        val = dict_counter[key]
        temp_tuple = (key, val)
        return_list.append(temp_tuple)

    return return_list

s = 'test test test'

print('my function')
for ch, freq in counter_items_for_2_symbols(s):
        print('ch: \'{}\' \tfreq: \'{}\''.format(ch, freq))
        print()

print('counter items')
for ch, freq in Counter(s).items():
        print('ch: \'{}\' \tfreq: \'{}\''.format(ch, freq))
        print()