# written by Patel
"""
input and output of a pickle file
"""

from file_abstract import File
import pickle

class PickleFile(File):
    def __init__(self):
        pass

    def get_input(self, file_name):
        with open(file_name, 'rb') as my_pickled_file:
            data_list = pickle.load(my_pickled_file)
        return (data_list)

    def save_data_to_new(self, file_name, data_list):
        with open(file_name, "wb") as my_pickled_file:
            pickle._dump(data_list, my_pickled_file)

