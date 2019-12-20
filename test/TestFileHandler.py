import os
import sys
import unittest
sys.path.append("../src/")
import FileHandler
import FileConversion
import ValidateNumber


class TestFileHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logs_folder = 'logs'
        cls.logs_file_name = 'log_test.txt'
        cls.data_folder = 'data'
        cls.data_file_name = 'source_data.txt'
        cls.data_file_name2 = 'source_data2.txt'
        cls.data_log_name2 = 'source_data2.logs'
        cls.number_to_check = ['345882865', '345882864']
        cls.response_check = [True, False]
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
        cls.return_list = ['123456789', '000000000', '111111111', '222222222', '333333333', '888888888']
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
        cls.validateNumber = ValidateNumber.ValidateNumber()

    @classmethod
    def tearDownClass(cls):
        file = os.path.join("..", cls.logs_folder, cls.data_log_name2)
        try:
            open(file)
        except:
            None
        os.remove(file)

    def setUp(self):
        self.fileHandler = FileHandler.FileHandler()
        self.fileConversion = FileConversion.FileConversion()

    def test_step1(self):
        print "----------- Starting step 1 -----------"
        self.fileHandler.folder = self.data_folder
        self.fileHandler.filename = self.data_file_name
        content = self.fileHandler.read_file()
        print "----------- Content of the file"
        print content
        result = self.fileConversion.text_to_number(content)
        print "----------- Number in the file"
        print result
        self.assertItemsEqual(result, self.return_list)
        print "----------- End of step 1 -----------"

    def test_step2(self):
        print "----------- Starting step 2 -----------"
        result = []
        for number in self.number_to_check:
            result.append(self.validateNumber.validate_checksum(number))
        print "----------- Number to check"
        print self.number_to_check
        print "----------- Result Checksum "
        print result
        self.assertItemsEqual(result, self.response_check)
        print "----------- End of step 2 -----------"

    def test_step3(self):
        print "----------- Starting step 3 -----------"
        self.fileHandler.folder = self.data_folder
        self.fileHandler.filename = self.data_file_name2
        content = self.fileHandler.read_file()
        print "----------- Content of the file"
        print content
        results = self.fileConversion.text_to_number(content)
        print "----------- Number in the file"
        print results
        self.assertItemsEqual(results, self.response_return_list_filename2)
        print "----------- Check Error in Numbers"
        for result in results:
            print self.validateNumber.check_ill_err(result)
        print "----------- Check Log information"
        self.validateNumber.validate_file(self.data_file_name2)
        self.fileHandler.folder = self.logs_folder
        self.fileHandler.filename = self.data_log_name2
        content = self.fileHandler.read_file()
        self.assertEqual(content.strip(), self.content_log.strip())
        print "----------- End of step 3 -----------"


if __name__ == '__main__':
    unittest.main()
