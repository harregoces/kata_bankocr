from ..Implementation.FileSourceData import FileSourceData


class SourceFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_source(source_type):
        try:
            if source_type == "File":
                return FileSourceData()
            raise AssertionError("Source not Found")
        except AssertionError as _e:
            print(_e)
