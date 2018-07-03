# created by Patel

from data_abstract import DataAbstract


class Data(DataAbstract):
    """
    Used by employee_data.py to return the data for a record
    """
    def load_data(self):
        pass

#   def add_data(self):
 #       pass

    def save_data(self):
        self.new_data = []
        return self._load_data()
