from functools import reduce


class ValidateNumber:
    number = []

    def __init__(self):
        pass

    def validate_number(self, number):
        number.reverse()
        self.number = number
        result = reduce(self.reduce_numbers, range(len(number)))
        return result % 11 == 0

    def reduce_numbers(self, x, y):
        n = y + 1
        if y == 1:
            result = self.number[x] + (n * self.number[y])
        else:
            result = x + (n * self.number[y])
        return result
