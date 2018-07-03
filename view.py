from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    """
    Interface for output implementation
    """
    @staticmethod
    @abstractmethod
    def display(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def error(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def success(text):
        """
        Output information
        :param text: A text string
        :return: None
        :Author: Vaishali Patel
        """
        pass

    @staticmethod
    @abstractmethod
    def display_data(data, ind=False):
        """
        Output data
        :param data: (list)
        :param ind: (Boolean)
        :return: None
        :Author: Vaishali Patel
        """
        pass

