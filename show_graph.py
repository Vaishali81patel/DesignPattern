from employee_get_data import GetEmployee
from console_view import ViewConsole as View
from employee_get_data import GetEmployee
from six import add_metaclass
import matplotlib.pyplot as plt
from graph_builder import GraphBuilder
from graph import Graph
from data import Data

class ShowGraph():
    """
    Represent the complex object under construction.
    """

    def __init__(self):
        self._shw = GetEmployee()  # Instace of GetEmployeeData
        self.__showGraph=[]

    def show_pie(self, line):
        # Draw Pies
        try:
            if len (self._shw.get_gender ()) == 0 or len (self._shw.get_bmi ()) == 0:
                raise ValueError ("No data to display.")
            # Draw gender
            if line.upper () == Data.GENDER.name:
                View.plot_pie (self._shw.get_gender (), "Gender Distribution")
            # Draw BMI
            if line.upper () == Data.BMI.name:
                View.plot_pie (self._shw.get_bmi (), "Body Mass Index (BMI)")
        except ValueError as e:
            View.info (e)
        except Exception as e:
            View.error (e)


    def show_bar(self, line):
        # Draw Bars
        try:
            if len (self._shw.get_gender ()) == 0 or len (self._shw.get_gender ()) == 0:
                raise ValueError ("No data to display.")
            # Draw gender
            if line.upper () == Data.GENDER.name:
                View.plot_bar (self._shw.get_gender (), "Gender Distribution")
            # Draw BMI
            if line.upper () == Data.BMI.name:
                View.plot_bar (self._shw.get_bmi (), "Body Mass Index (BMI)")
        except ValueError as e:
            View.info (e)
        except Exception as e:
            View.error (e)

    def show_scatter(self, line):
        # Draw Line Scatter
        try:
            if len (self._shw.get_gender()) == 0 or len (self._shw.get_salary()) == 0:
                raise ValueError ("No data to display.")
            # Draw gender
            if line.upper () == Data.GENDER.name:
                View.plot_bar (self._shw.get_gender(), "Gender Distribution")
            # Draw BMI
            if line.upper () == Data.SALARY.name:
                View.plot_bar (self._shw.get_salary(), "Salary Index (SALARY)")
        except ValueError as e:
            View.info (e)
        except Exception as e:
            View.error (e)

    def show_graph(self):
        return self.__showGraph
