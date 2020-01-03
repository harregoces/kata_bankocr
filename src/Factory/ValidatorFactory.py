from ..Implementation.ValidatorData import ValidatorData


class ValidatorFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_validator(validator_type):
        try:
            if validator_type == "Mod11":
                return ValidatorData()
            raise AssertionError("Validator not Found")
        except AssertionError as _e:
            print(_e)
