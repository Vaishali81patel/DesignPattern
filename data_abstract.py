# created by Pippa Crawshaw

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class DataAbstract:
    """
    Base class for DataCSV
    """
    def __init__(self, data_in):
        self._data = data_in

    @abstractmethod
    def load_data(self):
        pass;

    @abstractmethod
    def add_data(self):
        pass

    def save_data(self):
        pass
