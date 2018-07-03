from abc import ABCMeta, abstractmethod


class IDataAccess(metaclass=ABCMeta):
    """
    Interface for data access implementation
    :Author: Vaishali Patel
    """
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self, data: list):
        pass

