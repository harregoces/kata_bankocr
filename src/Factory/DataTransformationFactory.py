from ..Implementation.StringTransformation import StringTransformation


class DataTransformationFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_data_transformation(data_type):
        try:
            if data_type == "string":
                return StringTransformation()
            raise AssertionError("DataTransformation not Found")
        except AssertionError as _e:
            print(_e)
