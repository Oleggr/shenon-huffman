def text_format(text,
                low = True,
                only_letters = True,
                no_spaces = False,
                single_line = True):

    if low:
        text = text.lower()

    if only_letters:
        letters_list = []

        # for index in range(0, len(text) - 1):
        #     print(index)
        #     if not text[index].isalnum():
        #         text = text[:index] + ' ' + text[index + 1:]

        for elem in text:
            if elem.isalnum() or elem == ' ' or elem == '\n':
                letters_list.append(elem)

        text = ''

        for elem in letters_list:
            text += elem

    if no_spaces:
        letters_list = []

        for elem in text:
            if not elem == ' ':
                letters_list.append(elem)

        text = ''

        for elem in letters_list:
            text += elem

    if single_line:
        letters_list = []

        for elem in text:
            if not elem == '\n':
                letters_list.append(elem)

        text = ''

        for elem in letters_list:
            text += elem

    return text