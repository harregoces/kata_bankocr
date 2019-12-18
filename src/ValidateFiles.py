import sys
sys.path.append("../src/")
from FileHandler import FileHandler
from FileConversion import FileConversion
from ValidateNumber import ValidateNumber


class ValidateFiles:

    def __init__(self):
        pass

    def validate_file(self, file_name):
        file_logs = str(file_name.split('.')[0]) + ".logs"

        file_handler = FileHandler()
        file_handler.filename = file_name

        log_handler = FileHandler()
        log_handler.filename = file_logs
        log_handler.folder = "logs"

        file_conversion = FileConversion()
        validate_number = ValidateNumber()


        content = file_handler.read_file()
        list_numbers = file_conversion.text_to_number(content)
        for element in list_numbers:
            log_handler.write_in_file(
                "{0} {1} \r\n".format(str(element), validate_number.check_ill_err(element))
            )
