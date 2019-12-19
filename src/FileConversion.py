import string


class FileConversion:

    def __init__(self):
        pass

    number_0 = [[0, 2, 0], [1, 0, 1], [1, 2, 1]]
    number_1 = [[0, 0, 0], [0, 0, 1], [0, 0, 1]]
    number_2 = [[0, 2, 0], [0, 2, 1], [1, 2, 0]]
    number_3 = [[0, 2, 0], [0, 2, 1], [0, 2, 1]]
    number_4 = [[0, 0, 0], [1, 2, 1], [0, 0, 1]]
    number_5 = [[0, 2, 0], [1, 2, 0], [0, 2, 1]]
    number_6 = [[0, 2, 0], [1, 2, 0], [1, 2, 1]]
    number_7 = [[0, 2, 0], [0, 0, 1], [0, 0, 1]]
    number_8 = [[0, 2, 0], [1, 2, 1], [1, 2, 1]]
    number_9 = [[0, 2, 0], [1, 2, 1], [0, 2, 1]]

    def switch_number(self, arg):
        switcher = [
            [self.number_0, 0],
            [self.number_1, 1],
            [self.number_2, 2],
            [self.number_3, 3],
            [self.number_4, 4],
            [self.number_5, 5],
            [self.number_6, 6],
            [self.number_7, 7],
            [self.number_8, 8],
            [self.number_9, 9],
        ]
        for element in switcher:
            if element[0] == arg:
                return element[1]
        return "?"

    def text_to_number(self, content):
        content_split = self.split_text_in_list(content)
        return_list = []
        for element in content_split:
            matrix = self.split_list_in_matrix(element)
            self.matrix_to_number(matrix)
            number = []
            for n in matrix:
                number.append(self.switch_number(n))
            number = "".join(map(str, number))
            number = self.fix_text_to_number(number, matrix)
            return_list.append(number)
        return return_list


    def split_text_in_list(self, text):
        text = text.splitlines()
        list_return = []
        for index in range(0, len(text), 4):
            list_return.append([text[index], text[index + 1], text[index + 2]])
        return list_return

    def split_list_in_matrix(self, element):
        main_matrix = []
        maxlen = 3
        for index in range(0, len(element), 3):
            for i in range(0, 3*9, 3):
                matrix = [list(element[index][i:i + 3]) + [0]*(maxlen - len(element[index][i:i + 3])),
                          list(element[index + 1][i:i + 3]) + [0]*(maxlen - len(element[index + 1][i:i + 3])),
                          list(element[index + 2][i:i + 3]) + [0]*(maxlen - len(element[index + 2][i:i + 3]))
                          ]
                main_matrix.append(matrix)
        return main_matrix

    def matrix_to_number(self, matrix):
        for my_list in matrix:
            for element in my_list:
                for i in range(len(element)):
                    if element[i] == " ":
                        element[i] = 0
                    if element[i] == "|":
                        element[i] = 1
                    if element[i] == "_":
                        element[i] = 2
        return element

    def fix_text_to_number(self, number, matrix):
        for index in range(len(number)):
            posibilities = []
            for element_in_matrix in matrix[index]:

                for element_in_list in range(len(element_in_matrix)):
                    reserved = element_in_matrix[element_in_list]

                    # change the number to 0 if reserved is different
                    if reserved != 0:
                        element_in_matrix[element_in_list] = 0
                        i = self.switch_number(matrix[index])
                        if str(i).isdigit():
                            posibilities.append([index, i])

                    # change the number to 1
                    if reserved != 1:
                        element_in_matrix[element_in_list] = 1
                        i = self.switch_number(matrix[index])
                        if str(i).isdigit():
                            posibilities.append([index, i])

                    # change the number to 2
                    if reserved != 2:
                        element_in_matrix[element_in_list] = 2
                        i = self.switch_number(matrix[index])
                        if str(i).isdigit():
                            posibilities.append([index, i])

                    # return the number to previous value
                    element_in_matrix[element_in_list] = reserved

            print posibilities

        # return a list of posibilities for each number
        return number