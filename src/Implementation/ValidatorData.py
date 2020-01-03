from ..Interfaces.IValidatorData import IValidatorData
from ..Decorators.LoggerDecorator import LoggerDecorator


class ValidatorData(IValidatorData):
    __number = []

    @LoggerDecorator
    def check_ill_err(self, number):
        res = self.__check_ill(number)
        if res != '':
            return res
        else:
            return self.__check_err(number)

    def validate_checksum(self, number):
        try:
            int(number)
        except:
            return False

        number = list(number)
        number.reverse()
        self.__number = number
        result = reduce(self.__reduce_numbers, range(len(number)))
        return result % 11 == 0

    def __reduce_numbers(self, x, y):
        n = y + 1
        if y == 1:
            result = int(self.__number[x]) + (n * int(self.__number[y]))
        else:
            result = int(x) + (n * int(self.__number[y]))
        return result

    def __check_ill(self, number):
        if list(number).count('?') > 0:
            return 'ILL'
        return ''

    def __check_err(self, number):
        if not self.validate_checksum(number):
            return 'ERR'
        return ''
