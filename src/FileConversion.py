import string


class FileConversion:

    def __init__(self):
        pass

    def text_to_number(self, text):
        split_text = self.split_in_lines(text)
        for line in split_text:
            for l in line:
                print list(l)
                print "aqui"

    def split_in_lines(self, text):
        return_list = []
        index = 0
        return_msg = []
        return_msg1 = []
        for line in text.splitlines():
            if index < 4:
                return_msg.append(line)
                index += 1
                if index == 4:
                    index = 0
                    return_msg1.append(return_msg)
                    return_msg = []
                    if len(return_msg1) == 4:
                        return_list.append(return_msg1)
                        return_msg1 = []

        return return_list

f = FileConversion()
print f.text_to_number("123")