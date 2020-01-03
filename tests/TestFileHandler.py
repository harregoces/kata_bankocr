from src.Factory.SourceFactory import SourceFactory
from src.Factory.DataTransformationFactory import DataTransformationFactory
from src.Factory.ValidatorFactory import ValidatorFactory
import os
import unittest


class TestFileHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logs_folder = 'logs'
        cls.logs_file_name = 'log_test.txt'
        cls.__data_folder = 'data'
        cls.__data_file_name = 'source_data.txt'
        cls.__data_file_name2 = 'source_data2.txt'
        cls.data_log_name2 = 'source_data2.logs'
        cls.__number_to_check = ['345882865', '345882864']
        cls.__response_check = [True, False]
        cls.response_return_list_filename2 = ['000000051', '49006771?', '1234?678?', '664371495']
        cls.content_log = '000000051 \r\n'
        cls.content_log += '49006771? ILL\r\n'
        cls.content_log += '1234?678? ILL\r\n'
        cls.content_log += '664371495 ERR \r\n'
        cls.message = "    _  _     _  _  _  _  _ \r\n"
        cls.message += "  | _| _||_||_ |_   ||_||_|\r\n"
        cls.message += "  ||_  _|  | _||_|  ||_| _|\r\n"
        cls.message += "\r\n"
        cls.message += " _  _  _  _  _  _  _  _  _ \r\n"
        cls.message += "| || || || || || || || || |\r\n"
        cls.message += "|_||_||_||_||_||_||_||_||_|\r\n"
        cls.message += "\r\n"
        cls.message += "\r\n"
        cls.message += "  |  |  |  |  |  |  |  |  |\r\n"
        cls.message += "  |  |  |  |  |  |  |  |  |\r\n"
        cls.message += "\r\n"
        cls.message += " _  _  _  _  _  _  _  _  _ \r\n"
        cls.message += " _| _| _| _| _| _| _| _| _|\r\n"
        cls.message += "|_ |_ |_ |_ |_ |_ |_ |_ |_ \r\n"
        cls.message += "\r\n"
        cls.message += " _  _  _  _  _  _  _  _  _ \r\n"
        cls.message += " _| _| _| _| _| _| _| _| _|\r\n"
        cls.message += " _| _| _| _| _| _| _| _| _|\r\n"
        cls.message += "\r\n"
        cls.message += " _  _  _  _  _  _  _  _  _ \r\n"
        cls.message += "|_||_||_||_||_||_||_||_||_|\r\n"
        cls.message += "|_||_||_||_||_||_||_||_||_|\r\n"
        cls.message += "\r\n"
        cls.__return_list = ['123456789', '000000000', '111111111', '222222222', '333333333', '888888888']
        cls.message2 =  "    _  _     _  _  _  _  _ \r\n"
        cls.message2 += "  | _| _||_| _ |_   ||_||_|\r\n"
        cls.message2 += "  ||_  _|  | _||_|  ||_| _ \r\n"
        cls.message2 += "\r\n"
        cls.return_list2 = ['1234?678?']
        cls.return_list2_fixed = ['123456789']
        cls.message3 = " _  _  _  _  _  _  _  _    \r\n"
        cls.message3 += "| || || || || || || ||_   |\r\n"
        cls.message3 += "|_||_||_||_||_||_||_| _|  |\r\n"
        cls.message3 += "\r\n"
        cls.return_list3 = ['000000051']

    @classmethod
    def tearDownClass(cls):
        file = os.path.join("..", cls.logs_folder, cls.data_log_name2)
        try:
            open(file)
        except:
            None
            return
        os.remove(file)

    def test_step1(self):
        print "----------- Starting step 1 -----------"
        source_data = SourceFactory.get_source("File")
        source_data.folder = self.__data_folder
        source_data.filename = self.__data_file_name
        content = source_data.get_data()
        print "----------- Content of the file"
        print content
        data_transform = DataTransformationFactory.get_data_transformation("string")
        numbers = data_transform.transform_data(content)
        print "----------- Number in the file"
        print numbers
        self.assertItemsEqual(numbers, self.__return_list)
        print "----------- End of step 1 -----------"

    def test_step2(self):
        print "----------- Starting step 2 -----------"
        validator_factory = ValidatorFactory.get_validator("Mod11")
        result = []
        for number in self.__number_to_check:
            result.append(validator_factory.validate_checksum(number))
        print "----------- Number to check"
        print self.__number_to_check
        print "----------- Result Checksum "
        print result
        self.assertItemsEqual(result, self.__response_check)
        print "----------- End of step 2 -----------"

    def test_step3(self):
        print "----------- Starting step 3 -----------"
        source_data = SourceFactory.get_source("File")
        source_data.folder = self.__data_folder
        source_data.filename = self.__data_file_name
        content = source_data.get_data()
        print "----------- Content of the file"
        print content
        data_transform = DataTransformationFactory.get_data_transformation("string")
        numbers = data_transform.transform_data(content)
        print "----------- Number in the file"
        print numbers
        self.assertItemsEqual(numbers, self.__return_list)
        print "----------- Check Error in Numbers"
        validator_data = ValidatorFactory.get_validator("Mod11")
        for number in numbers:
            validator_data.check_ill_err(number)
        print "----------- End of step 3 -----------"

    def test_step4(self):
        print "----------- Starting step 4 -----------"
        source_data = SourceFactory.get_source("File")
        source_data.folder = self.__data_folder
        source_data.filename = self.__data_file_name2
        content = source_data.get_data()
        print "----------- Content of the file"
        print content
        data_transform = DataTransformationFactory.get_data_transformation("string")
        numbers = data_transform.get_possibilities(content)
        print "----------- Number in the file"
        print numbers
        print "----------- End of step 4 -----------"


if __name__ == '__main__':
    unittest.main()
