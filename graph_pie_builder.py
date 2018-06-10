# written by Patel
"""
Basic pie chart

"""

import matplotlib.pyplot as plt
from graph_builder import GraphBuilder


class PieChartBuilder(GraphBuilder):
    def setup_gender_graph(self):
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()

        # startangle = 90 - everything is
        # rotated counter-clockwise by 90 degrees,
        #  and the first lable slice starts on the positive y-axis.
        ax1.pie(self._sizes, explode=explode, labels=self._labels,
                autopct='%1.1f%%', shadow=True, startangle=90)

        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')

        plt.title("Ratio of Females vs Males")
        self._plt = plt
