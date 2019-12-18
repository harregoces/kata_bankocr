import string


class FileConversion:

    def __init__(self):
        pass

    number_0 = -810165527
    number_1 = 780621982
    number_2 = 276169731
    number_3 = 1561235153
    number_4 = 1343304099
    number_5 = 617962149
    number_6 = 369237634
    number_7 = -1832969678
    number_8 = 1365986198
    number_9 = 522434841

    def switch_number(self, arg):
        switcher = {
            self.number_0: 0,
            self.number_1: 1,
            self.number_2: 2,
            self.number_3: 3,
            self.number_4: 4,
            self.number_5: 5,
            self.number_6: 6,
            self.number_7: 7,
            self.number_8: 8,
            self.number_9: 9,
        }
        return switcher.get(arg, "?")

    def text_to_number(self, text):
        split_text = text.splitlines()
        number_in_text = []
        for line in range(0, len(split_text), 4):
            number_in_line = []
            for n in range(0, 3*9, 3):
                number = []

                for pos in range(3):
                    for pos2 in range(3):
                        result = self.set_position(split_text, line + pos, n + pos2, pos, pos2)
                        if result:
                            number.append(result)

                number_in_line.append(self.switch_number(hash(tuple(number))))
            number_in_text.append("".join(map(str, number_in_line)))
        return number_in_text

    def fill_text(self, split_text, index):
        if len(split_text[index]) == 0:
            split_text[index] = " " * 29
        return split_text[index]

    def set_position(self, split_text, index, index2, pos, pos2):
        try:
            if len(split_text[index][index2].strip()) > 0:
                return tuple((pos, pos2))
        except IndexError:
            return None
