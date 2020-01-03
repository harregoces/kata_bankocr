from ..Interfaces.IDataTransform import IDataTransform


class StringTransformation(IDataTransform):

    __number_0 = [[0, 2, 0], [1, 0, 1], [1, 2, 1]]
    __number_1 = [[0, 0, 0], [0, 0, 1], [0, 0, 1]]
    __number_2 = [[0, 2, 0], [0, 2, 1], [1, 2, 0]]
    __number_3 = [[0, 2, 0], [0, 2, 1], [0, 2, 1]]
    __number_4 = [[0, 0, 0], [1, 2, 1], [0, 0, 1]]
    __number_5 = [[0, 2, 0], [1, 2, 0], [0, 2, 1]]
    __number_6 = [[0, 2, 0], [1, 2, 0], [1, 2, 1]]
    __number_7 = [[0, 2, 0], [0, 0, 1], [0, 0, 1]]
    __number_8 = [[0, 2, 0], [1, 2, 1], [1, 2, 1]]
    __number_9 = [[0, 2, 0], [1, 2, 1], [0, 2, 1]]

    def __switch_number(self, arg):
        switcher = [
            [self.__number_0, 0],
            [self.__number_1, 1],
            [self.__number_2, 2],
            [self.__number_3, 3],
            [self.__number_4, 4],
            [self.__number_5, 5],
            [self.__number_6, 6],
            [self.__number_7, 7],
            [self.__number_8, 8],
            [self.__number_9, 9],
        ]
        for element in switcher:
            if element[0] == arg:
                return element[1]
        return "?"

    def __text_to_number(self, content):
        content_split = self.__split_text_in_list(content)
        return_list = []
        for element in content_split:
            matrix = self.__split_list_in_matrix(element)
            self.__matrix_to_number(matrix)
            number = []
            for n in matrix:
                number.append(self.__switch_number(n))
            number = "".join(map(str, number))
            return_list.append(number)
        return return_list

    @staticmethod
    def __split_text_in_list(text):
        text = text.splitlines()
        list_return = []
        for index in range(0, len(text), 4):
            list_return.append([text[index], text[index + 1], text[index + 2]])
        return list_return

    @staticmethod
    def __split_list_in_matrix(element):
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

    @staticmethod
    def __matrix_to_number(matrix):
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

    def transform_data(self, data):
        return self.__text_to_number(data)

    def get_posibilites(self, content):
        content_split = self.__split_text_in_list(content)
        return_list = {}
        for element in content_split:
            matrix = self.__split_list_in_matrix(element)
            self.__matrix_to_number(matrix)
            number = []
            for n in matrix:
                number.append(self.__switch_number(n))
            number = "".join(map(str, number))
            possibilities = self.__fix_text_to_number(number, matrix)
            return_list[number] = possibilities
        return return_list

    def __fix_text_to_number(self, number, matrix):
        possibilities = {}
        if number.count("?") > 1:
            return

        if number.count("?") == 1:
            index = number.find("?")
            for element_in_matrix in matrix[index]:
                for element_in_list in range(len(element_in_matrix)):
                    reserved = element_in_matrix[element_in_list]
                    # change the number to 0 if reserved is different
                    if reserved != 0:
                        element_in_matrix[element_in_list] = 0
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # change the number to 1
                    if reserved != 1:
                        element_in_matrix[element_in_list] = 1
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # change the number to 2
                    if reserved != 2:
                        element_in_matrix[element_in_list] = 2
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # return the number to previous value
                    element_in_matrix[element_in_list] = reserved
            return possibilities

        for index in range(len(number)):
            for element_in_matrix in matrix[index]:
                for element_in_list in range(len(element_in_matrix)):
                    reserved = element_in_matrix[element_in_list]

                    # change the number to 0 if reserved is different
                    if reserved != 0:
                        element_in_matrix[element_in_list] = 0
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # change the number to 1
                    if reserved != 1:
                        element_in_matrix[element_in_list] = 1
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # change the number to 2
                    if reserved != 2:
                        element_in_matrix[element_in_list] = 2
                        i = self.__switch_number(matrix[index])
                        if str(i).isdigit():
                            if index in possibilities.keys():
                                possibilities[index].append(i)
                            else:
                                possibilities[index] = [i]

                    # return the number to previous value
                    element_in_matrix[element_in_list] = reserved
        return possibilities
