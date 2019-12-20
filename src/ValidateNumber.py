from functools import reduce
import sys
from FileHandler import FileHandler
import FileConversion
import ValidateNumber


class ValidateNumber:
    number = []

    def __init__(self):
        pass

    def validate_checksum(self, number):
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
        if not self.validate_checksum(number):
            return 'ERR'
        return ''

    def check_ill_err(self, number):
        res = self.check_ill(number)
        if res != '':
           return res
        else:
            return self.check_err(number)

    def validate_file(self, file_name):
        file_logs = str(file_name.split('.')[0]) + ".logs"

        file_handler = FileHandler()
        file_handler.filename = file_name

        log_handler = FileHandler()
        log_handler.filename = file_logs
        log_handler.folder = "logs"

        file_conversion = FileConversion.FileConversion()


        content = file_handler.read_file()
        list_numbers = file_conversion.text_to_number(content)
        for element in list_numbers:
            log_handler.write_in_file(
                "{0} {1}\r\n".format(str(element), self.check_ill_err(element))
            )
