from cmd import Cmd
from csv import Error as CSVError
from data_validator import DataValidator
from console_view import ViewConsole as View
from graph_director import GraphDirector
from graph_builder import GraphBuilder
from show_graph import ShowGraph
from graph import Graph
from employee_get_data import GetEmployee
from data import Data
from sys import argv
from file_types import FileTypes
import os

class InterpreterController (Cmd):
    _input_file = ''
    _output_file = ''
    _data_list = []

    #  _graph = None
    # This class is a controller class which enable interpreter (model) and
    # View (Console View) to interconnect with each other and
    # This class also defined command loop enables \
    # the associate commands invoke
    #
    # Written By: Patel
    #
    def __init__(self):
        Cmd.__init__(self)  # Initialize cmd interface here
        self.prompt = ">>> "  # Initialize prompt
        self._vld = DataValidator()  # Object of DataValidator, for validating data
 #       self._graph = GraphDirector()
#        self._grp = Graph()
        self._graph = ShowGraph()
        self._shw = GetEmployee() # Instace of GetEmployeeData
        self.intro = "WELCOME TO THE EMPLOYEE DATABASE MANAGEMENT CONSOLE \n ENTER A KEYWORD TO START. FOT HELP, ENTER \"help\"."
        # Welcome information

    def do_select(self, line):
        """
        Select a data source
        :param line: <String> Source name
        :return: None
        :Author: Vaishali Patel
        """
        # Available data sources
        options = "-csv", "-db"
        args = list (arg.lower () for arg in str (line).split ())

        try:
            # Check if the input data source is available in this program or not
            if args[0] not in options:
                raise ValueError ("The data resource is not available.")
            else:
                # Code for initialise CSV data source
                if args[0] == "-csv":
                    try:
                        if len (args) == 1:
                            self._shw.select_source (args[0][1:], "employeeinfo.csv")
                            View.warning (
                                "No CSV file path specified. A default file \"employeeinfo.csv\" will be used.")
                        elif len (args) == 2:
                            self._shw.select_source (args[0][1:], args[1])
                        elif len (args) == 3:
                            if args[1] == "-a":
                                self._shw.select_source (args[0][1:], args[2], True)
                    except (CSVError, OSError) as e:
                        View.error (e)
                    except Exception as e:
                        View.error (e)
                    else:
                        View.success ("Data source CSV is selected.")

                # Code for initialise database source
                elif args[0] == "-db":
                    try:
                        self._shw.select_source (args[0][1:])
                    except (ConnectionError, TypeError) as e:
                        View.error (e)
                    except Exception as e:
                        View.error (e)
                    else:
                        View.success ("Data source Database is selected.")

                # Code for initialise XXXX data source
                else:
                    pass
        # Catch and display error message
        except ValueError as e:
            View.error (str (e) + "\n")
            View.help_select ()
        except Exception as e:
            View.error (e)

    def do_add(self, line):
        """
        # This function enable to add employee data into system
        # Which basically give all the available option to the user
        # parse: splits the given sequence of characters or values (text)
        # into smaller parts based on some rules
        #
        # Written By: Patel
        :param line: <EMPID> <Age> <Gender> <Sales> <BMI> <Salary> <Birthday>
        :return: None
        """
        # Split the input argument to obtain the data
        raw_data = list (arg.lower () for arg in str (line).split ())

        try:
            # Check if input data has 7 data fields
            if not len (raw_data) == len (Data):
                raise AttributeError ("Please input correct data.")
            else:
                # Check and wash data by check_all() of DataValidator
                result = self._vld.check_all (raw_data)
                # Check if there is any None which stands for invalid input
                if None in result:
                    key = 0
                    # build a list of name list
                    items = list (map (lambda i: i.name, Data))
                    e_str = ""
                    while key < len (result):
                        if result[key] is None:
                            # Left alignment
                            e_str += "{:<10}".format (items[key])
                        key += 1
                    raise ValueError ("The following field(s) is invalid:\n%s" % e_str)
                else:
                    self._shw.add_data (result)
        except (AttributeError, ValueError) as e:
            View.error (str (e) + "\n")
            View.help_add ()
        except CSVError as e:
            View.error (e)
        except Exception as e:
            View.error (e)
        else:
            View.success ("Add data")

    def do_save(self, arg):
        """
        Save data to specified data source# This function enable to access dict option for respective file
        # to be stored in the system
        # Raise Exception error if unable to do so
        #
        # Written By: Patel
        #
        :param arg: arg
        :return: None
        """
        # If no data source selected, prompt user to do so.
        try:
            self._shw.save_data ()
        except ValueError as e:
            View.info (e)
        except (OSError, AttributeError) as e:
            View.error (e)
        except Exception as e:
            View.error (e)
        else:
            View.success ("Data is saved")

    def do_show(self, line):
        # Get all instructions# This function enable to create dictionary option
        # to respective commands and the system find matches
        # to the respective option to show individual map / view
        #
        # Written By: Patel
        #
        args = list (arg.lower() for arg in str (line).split())

        # Those commands are required single arguments
        # single_commands = ["-a"]
        # Those commands are required two arguments
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

        else:
            View.info ("Invalid command line.\n")
            View.help_show ()


    def do_graph_show(self, line):
        _graph = None
        graph_director = GraphDirector (None)
        plot_commands = ["-p", "-b", "-c"]

        if args[0] in plot_commands:
            try:
                if len (args) == 1:
                    raise IndexError ("Incomplete command line.")

                if args[0] == "-p":
                    graph_builder = self._graph.show_pie(self._data_list)
                    graph_director.set_builder(graph_builder)
                if args[0] == "-b":
                    graph_builder = self._graph.show_bar(self._data_list)
                    graph_director.set_builder (graph_builder)
                if args[0] == "-c":
                    graph_builder = self._graph.show_scatter(self._data_list)
                    graph_director.set_builder (graph_builder)

            except IndexError as e:
                View.error (str (e) + "\n")
                View.help_show()
        else:
            View.info ("Invalid command line.\n")
            View.help_show ()

            graph_director.construct()
            _graph = graph_builder.get_graph()
        return _graph

    @staticmethod
    def help_show():
        View.help_show ()

    @staticmethod
    def help_add():
        View.help_add ()

    @staticmethod
    def help_save():
        View.help_save ()

    @staticmethod
    def help_select():
        View.help_select ()

    @staticmethod
    def help_quit():
        View.help_quit ()

    def do_quit(self, line):
        arg = str (line).lower ()
        if not arg == "-f" and not len (self._shw.new_data) == 0:
            View.warning ("The new data hasn't been saved. Enter \"quit -f\" to quit without saving.")
        else:
            View.display ("Thanks for using. Bye!")
            return True

    def check_valid_file_name(self, file_name, input_output):
        """
        Checks to make sure the file_name exists and if it
        has a valid file extension
        :param file_name:
        :param input_output:
        :return:
        """
        if self.check_file_exists (file_name):
            if self.check_file_name_extensions (file_name, input_output):
                return True
            else:
                return False
        else:
            print ("File does not exist")
            return False

    def check_file_name_extensions(self, file_name, input_output):
        """
        Checks the file extension against the possible extensions set up
        in the class variable _extension_types
        :param file_name:
        :param input_output:
        :return:
        """
        file_type = FileTypes ()
        extension_types = file_type.get_extension_types ()
        for extension in extension_types:
            if file_name.endswith (extension):
                if input_output == 'input':
                    self._input_file = file_type.get_file_type (extension)
                else:
                    self._output_file = file_type.get_file_type (extension)
                return True
        print ("File name must end with:")
        for extension in extension_types:
            print (extension)
        return False


if __name__ == "__main__":
    ctl = InterpreterController ()
    ctl.cmdloop ()
