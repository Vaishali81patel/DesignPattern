# written by Patel

from abc import ABCMeta, abstractmethod
from file_handler import FileHandler
from file_database import Database
from file_pickle import PickleFile


class FileTypesAbstract(metaclass=ABCMeta):
    def __init__(self):
        self.file_types = {"csv": FileHandler(),
                      "db": Database(),
                      "pickle": PickleFile()}

    @abstractmethod
    def create_file_type(self, extension):
        pass

    @abstractmethod
    def get_file_type(self):
        pass
