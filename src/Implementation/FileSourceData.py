import os
from ..Interfaces.ISourceData import ISourceData


class FileSourceData(ISourceData):

    root_folder = ".."
    folder = "data"
    filename = ''

    def __get_directory(self):
        return os.path.join(self.root_folder, self.folder)

    def __get_content_file_name(self):
        return os.path.join(self.root_folder, self.folder, self.filename)

    def __read_file(self):
        content = []
        try:
            f = open(self.__get_content_file_name(), "r+")
        except:
            raise Exception("File not found: {0}".format(self.filename))
        if f.mode == 'r+':
            content = f.read()
        f.close()
        return content

    def get_data(self):
        return self.__read_file()
