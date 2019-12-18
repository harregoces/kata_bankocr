from functools import reduce


class ValidateNumber:
    number = []

    def __init__(self):
        pass

    def validate_number(self, number):
        try:
            int(number)
        except:
            return False

        number = list(number)
        number.reverse()
        self.number = number
        result = reduce(self.reduce_numbers, range(len(number)))
        return result % 11 == 0

    def reduce_numbers(self, x, y):
        n = y + 1
        if y == 1:
            result = int(self.number[x]) + (n * int(self.number[y]))
        else:
            result = int(x) + (n * int(self.number[y]))
        return result

    def check_ill(self, number):
        if list(number).count('?') > 0:
            return 'ILL'
        return ''

    def check_err(self, number):
        if not self.validate_number(number):
            return 'ERR'
        return ''

    def check_ill_err(self, number):
        res = self.check_ill(number)
        if res != '':
           return res
        else:
            return self.check_err(number)
