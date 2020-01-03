from abc import ABCMeta, abstractmethod


class IDataTransform:

    __metaclass__ = ABCMeta

    @abstractmethod
    def transform_data(self, data):
        """The data source interface"""

    @abstractmethod
    def get_possibilities(self, content):
        """The get posibilities interface"""
