from abc import ABCMeta, abstractmethod


class IValidatorData:
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate_checksum(self, number):
        """The validate data interface"""

    @abstractmethod
    def check_ill_err(self, number):
        """The check error interface"""
