import os


class FileHandler:

    def __init__(self):
        pass

    root_folder = ".."
    folder = "data"
    filename = ''

    def write_in_file(self, message):
        f = open(self.get_content_file_name(), "w+")
        result = f.write(message)
        f.close()
        return result

    def get_content_file_name(self):
        return os.path.join(self.root_folder, self.folder, self.filename)

    def get_directory(self):
        return os.path.join(self.root_folder, self.folder)

    def read_file(self):
        content = []
        f = open(self.get_content_file_name(), "r")
        if f.mode == 'r':
            content = f.read()
        f.close()
        return content

    def get_files_in_directory(self):
        return os.listdir(self.get_directory())
