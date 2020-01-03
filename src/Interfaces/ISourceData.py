from abc import ABCMeta, abstractmethod


class ISourceData:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_data(self):
        """The data source interface"""
