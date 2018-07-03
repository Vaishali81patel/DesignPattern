# written by Patel
"""
input and output of a pickle file
"""

from file_abstract import IDataAccess
from os import path, makedirs
import pickle

class PickleFile(IDataAccess):
    def __init__(self):
        pass

    def read(self, file_name):
        with open(file_name, 'rb') as my_pickled_file:
            data_list = pickle.load(my_pickled_file)
        return (data_list)

    def save(self, file_name, data_list):
        with open(file_name, "wb") as my_pickled_file:
            pickle._dump(data_list, my_pickled_file)

