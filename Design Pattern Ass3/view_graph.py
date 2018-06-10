import matplotlib.pyplot as plt
import numpy as np
from data import Data

class ViewGraph:

    @staticmethod
    @abstractmethod
    def plot_pie(data, title=""):
        """
        Plot a pie chart for gender, BMI
        :param data: data dictionary
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass


    @staticmethod
    @abstractmethod
    def plot_bar(data, title=""):
        """
        Plot a vertical bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass


    @staticmethod
    @abstractmethod
    def plot_barh(data, title=""):
        """
        Plot a horizontal bar chart for sales, salary, age...
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass


    @staticmethod
    @abstractmethod
    def plot_Scatter(data, title=""):
        """
        Plot a Scatter bar chart for men vs women
        :param data: dictionary,
        :param title: string
        :return: None
        :Author: Vaishali Patel
        """
        pass
