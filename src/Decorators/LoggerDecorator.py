from functools import update_wrapper, partial
import os
import datetime


class LoggerDecorator(object):
    __root_folder = ".."
    __folder = "logs"
    __filename = ''

    def __init__(self, original_function):
        update_wrapper(self, original_function)
        self.original_function = original_function
        now = datetime.datetime.now()
        self.__filename = "{}_{}_{}.log".format(now.day, now.month, now.year)

    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)

    def __call__(self, obj,  *args, **kwargs):
        result = self.original_function(obj, *args, **kwargs)
        for arg in args:
            self.__write_log(arg, result)
        return result

    def __get_directory(self):
        return os.path.join(self.__root_folder, self.__folder)

    def __get_log_file_name(self):
        return os.path.join(self.__root_folder, self.__folder, self.__filename)

    def __write_log(self, number, result):
        try:
            f = open(self.__get_log_file_name(), "a+")
        except:
            raise Exception("File not found: {0}".format(self.__get_log_file_name()))
        if f.mode == 'a+':
            f.write("{} {}\n".format(number, result))
        f.close()
