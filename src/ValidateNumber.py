from functools import reduce


class ValidateNumber:

    def __init__(self):
        pass

    def validate_number(self, number):
        number.reverse()
        result = reduce(lambda x, y: number[x] + ((y + 1) * number[y]) if x == 0 else x + ((y + 1) * number[y]),
                        range(len(number)))
        return result % 11 == 0
