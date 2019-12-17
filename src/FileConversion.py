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
        return switcher.get(arg, "Invalid Number")

    def text_to_number(self, text):
        split_text = text.splitlines()
        number_in_text = []
        for line in range(0, len(split_text), 4):
            number_in_line = []
            for n in range(0, 3*9, 3):
                number = []
                if len(split_text[line]) == 0:
                    split_text[line] = " "*29
                if len(split_text[line + 1]) == 0:
                    split_text[line + 1] = " "*27
                if len(split_text[line + 2]) == 0:
                    split_text[line + 2] = " "*27

                if len(split_text[line][n].strip()) > 0:
                    number.append((0, 0))
                if len(split_text[line][n + 1].strip()) > 0:
                    number.append((0, 1))
                if len(split_text[line][n + 2].strip()) > 0:
                    number.append((0, 2))

                if len(split_text[line + 1][n].strip()) > 0:
                    number.append((1, 0))
                if len(split_text[line + 1][n + 1].strip()) > 0:
                    number.append((1, 1))
                if len(split_text[line + 1][n + 2].strip()) > 0:
                    number.append((1, 2))

                if len(split_text[line + 2][n].strip()) > 0:
                    number.append((2, 0))
                if len(split_text[line + 2][n + 1].strip()) > 0:
                    number.append((2, 1))
                if len(split_text[line + 2][n + 2].strip()) > 0:
                    number.append((2, 2))

                number_in_line.append(int(self.switch_number(hash(tuple(number)))))
            number_in_text.append(number_in_line)
        return number_in_text