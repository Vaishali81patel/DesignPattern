"""
Purpose.  Builder
The monolithic design supports a single representation.
The Builder design allows a different representation
per Builder derived class,
and the common input and parsing have been defined in the Director class.
The Director constructs, the Builder returns the result.
"""

from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
from data import Data


class Array(object):
    def __init__(self):
        self.lst = []
		
	    def do_show(self, line):
        # Get all instructions# This function enable to create dictionary option
        # to respective commands and the system find matches
        # to the respective option to show individual map / view
        #
        # Written By: Patel
        #
        args = list (arg.lower () for arg in str (line).split ())

        # Those commands are required single arguments
        # single_commands = ["-a"]
        # Those commands are required two arguments
        plot_commands = ["-p", "-b", "-c"]

        # Show data table
        if args[0] == "-t":
            if len (self._shw.data) == 0 and len (self._shw.new_data) == 0:
                View.info ("No data to display.")
            if not len (self._shw.data) == 0:
                View.display ("ORIGINAL DATA:")
                View.display_data (self._shw.data, ind=True)
            if not len (self._shw.new_data) == 0:
                View.display ("\nNEW DATA:")
                View.display_data (self._shw.new_data, ind=True)
                View.display ("\n(Input command \"save\" to save the new data)")

        elif args[0] in plot_commands:
            try:
                if len (args) == 1:
                    raise IndexError ("Incomplete command line.")

                if args[0] == "-p":
                    self.show_pie (args[1])
                if args[0] == "-b":
                    self.show_bar (args[1])
                if args[0] == "-c":
                    self.show_scatter (args[1])

            except IndexError as e:
                View.error (str (e) + "\n")
                View.help_show ()
        else:
            View.info ("Invalid command line.\n")
            View.help_show ()

    
class Builder(metaclass=ABCMeta):
    def __init__(self):
        self.data = Array()

    def get_result(self):
        return self.data

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


class BuilderOne(Builder):
    
	@staticmethod
    def plot_pie(data, title=""):
        # Get labels and sizes from the data
        labels, values = list(data.keys()), list(data.values())

        # Show numbers on labels
        index = 0
        while index < len(labels):
            labels[id] = "{0} ({1})".format(labels[index], values[index])
            index += 1

        # Create a figure and a set of subplots
        fq, ax = plt.subplots()

        # Set labels, start angle, and the label format (e.g.: 35.0%)
        ax.pie(values, labels=labels, startangle=90, autopct="%0.1f%%")

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis("equal")

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_bar(data, title=""):
        # Get labels and sizes from the data
        labels, y = list(data.keys()), list(data.values())

        # Calculate numbers of items on x axis
        x = np.arange(len(labels))

        # Width of bars
        width = 0.5

        # Set X, Y, bar width and bar colour
        plt.bar(x, y, width, color="#00FFFF")

        # Set labels for X items
        plt.xticks(x, labels)

        # Show diagram grid
        plt.grid(True)

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

    @staticmethod
    def plot_barh(data, title=""):
        # Get labels and sizes from the data
        labels, x = list(data.keys()), list(data.values())

        # Calculate numbers of items on y axis
        y = np.arange(len(labels))

        # Width of bars
        width = 0.2

        # Set Y, X, bar width and bar colour
        plt.barh(y, x, width, color="#ADD8E6")

        # Set labels for Y items
        plt.yticks(y, labels)

        # Show diagram grid
        plt.grid(True)

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

    # Author: Vaishali Patel

    @staticmethod
    def plot_scatter(data, title=""):
        # Get labels and sizes from the data
        labels, values = list(data.keys()), list(data.values())

        # Show numbers on labels
        index = 0
        while index < len(labels):
            labels[id] = "{0}({1})".format(labels[index], values[index])
            index += 1

        # Create a figure and a set of subplots
        fq, ax = plt.subplots()

        # Set labels, start angle, and the label format (e.g.: 35.0%)
        ax.pie(values, labels=labels, startangle=90, autopct="%0.1f%%")

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis("equal")

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title(title.upper())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()


class Director(object):
    def __init__(self, b):
        self.bldr = b

    def set_builder(self, b):
        self.bldr = b

    def construct(self, inputs):
        for item in inputs:
            if item[0] == -p':
                self.bldr.plot_pie(item[1])
            elif item[0] == '-b':
                self.bldr.plot_bar(item[1])
			elif item[0] == '-c':
                self.bldr.plot_scatter(item[1])
				

if __name__ == "__main__":
    input_data = ("-b", "-p", "-c")

    one = BuilderOne()
    dir = Director(one)
    dir.construct(input_data)
    one.get_result().get_graph()

    