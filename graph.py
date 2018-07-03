from employee_get_data import GetEmployee
from abc import ABCMeta, abstractmethod
from six import add_metaclass
import matplotlib.pyplot as plt
import numpy as np
from data import Data
from graph_builder import GraphBuilder


class Graph():

    def plot_pie(data, title=""):
        # Get labels and sizes from the data
        labels, values = list (data.keys ()), list (data.values ())

        # Show numbers on labels
        index = 0
        while index < len (labels):
            labels[id] = "{0} ({1})".format (labels[index], values[index])
            index += 1

        # Create a figure and a set of subplots
        fq, ax = plt.subplots ()

        # Set labels, start angle, and the label format (e.g.: 35.0%)
        ax.pie (values, labels=labels, startangle=90, autopct="%0.1f%%")

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis ("equal")

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title (title.upper ())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show ()


    @staticmethod
    def plot_bar(data, title=""):
        # Get labels and sizes from the data
        labels, y = list (data.keys ()), list (data.values ())

        # Calculate numbers of items on x axis
        x = np.arange (len (labels))

        # Width of bars
        width = 0.5

        # Set X, Y, bar width and bar colour
        plt.bar (x, y, width, color="#00FFFF")

        # Set labels for X items
        plt.xticks (x, labels)

        # Show diagram grid
        plt.grid (True)

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title (title.upper ())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show ()


    @staticmethod
    def plot_scatter(data, title=""):
        # Get labels and sizes from the data
        labels, values = list (data.keys ()), list (data.values ())

        # Show numbers on labels
        index = 0
        while index < len (labels):
            labels[id] = "{0}({1})".format (labels[index], values[index])
            index += 1

        # Create a figure and a set of subplots
        fq, ax = plt.subplots ()

        # Set labels, start angle, and the label format (e.g.: 35.0%)
        ax.pie (values, labels=labels, startangle=90, autopct="%0.1f%%")

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis ("equal")

        # If the title is set, then convert to uppercase and display it
        if not title == "":
            plt.title (title.upper ())

        # Set of an interactive diagram is required
        # plt.interactive(True)
        plt.show()

