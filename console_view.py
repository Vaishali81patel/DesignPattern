from view import View
import matplotlib.pyplot as plt
import numpy as np
from data import Data


class ViewConsole(View):
    @staticmethod
    def display(text):
        print(text)

    @staticmethod
    def error(text):
        print("Error: %s" % text)

    @staticmethod
    def success(text):
        print("Succeed: %s" % text)

    @staticmethod
    def warning(text):
        print("Warning: %s" % text)

    @staticmethod
    def info(text):
        print("Info: %s" % text)

    @staticmethod
    def display_data(data, ind=False):
        ind_txt = "\t" if ind is True else ""

        print(ind_txt + "{:<8}{:<9}{:<6}{:<8}{:<15}{:<9}{:<15}"
              .format(Data.EMPID.name,
                      Data.GENDER.name,
                      Data.AGE.name,
                      Data.SALES.name,
                      Data.BMI.name,
                      Data.SALARY.name,
                      Data.BIRTHDAY.name))
        print(ind_txt + ("-" * 70))
        for row in data:
            print(ind_txt + "{:<8}{:<9}{:<6}{:<8}{:<15}{:<9}{:<15}"
                  .format(row[Data.EMPID.name],
                          row[Data.GENDER.name],
                          row[Data.AGE.name],
                          row[Data.SALES.name],
                          row[Data.BMI.name],
                          row[Data.SALARY.name],
                          row[Data.BIRTHDAY.name]))

    @staticmethod
    def help_show():
        print("USAGE:")
        print("\tshow <-OPTION> <OBJECT>")
        print("\nOPTIONS:")
        print("\t-t : Shows all data tables.")
        print("\t-b : Shows a bar graph of the total sales made by males verse the total sales made by female.")
        print("\t-p : Shows a pie chart of the percentage of female workers verse male workers")
        print("\t-c : Shows a scatter plot graph of peoples age verse their salary.")
        print("\t-i : Shows a pie chart of the BMI of a set of people.")
        print("\nEXAMPLES:")
        print("\t{:.<35}{:<50}".format("show -t", "Show all data"))
        print("\t{:.<35}{:<50}".format("show -b bmi", "Show bar chart of bmi"))
        print("\t{:.<35}{:<50}".format("show -p gender", "Show pie chart of gender"))
        print ("\t{:.<35}{:<50}".format("show -c salary", "Show scatter line chart of "))

    @staticmethod
    def help_add():
        print("USAGE:")
        print("\tadd <EMPID> <GENDER> <AGE> <SALES> <BMI> <SALARY> <BIRTHDAY>")

        print("\nDATA FORMAT:")
        print("\t{:.<15}{:<20}".format("EMPID", "[A-Z][0-9]{3} e.x.: M123"))
        print("\t{:.<15}{:<20}".format("GENDER", "(M|F)  e.x.: F"))
        print("\t{:.<15}{:<20}".format("AGE", "[0-9]{2}  e.x.: 28"))
        print("\t{:.<15}{:<20}".format("SALES", "[0-9]{3} e.x.: 100"))
        print("\t{:.<15}{:<20}".format("BMI", "(Normal|Overweight|Obesity|Underweight) e.x.: Normal"))
        print("\t{:.<15}{:<20}".format("SALARY", "[0-9]{2-3} e.x.: 200"))
        print("\t{:.<15}{:<20}".format("BIRTHDAY", "[1-31]-[1-12]-[0-9]{4} e.x.: 1990-10-21"))

        print("\nEXAMPLES:")
        print("\t{:.<60}{:<60}".format("add B123 F 28 100 normal 200 01-01-1990",
                                       "Add a employee with specified information."))

    @staticmethod
    def help_save():
        print("USAGE:")
        print("\tsave")
        print("\nDESCRIPTION:")
        print("\tSave new data to the selected data source.")

    @staticmethod
    def help_select():
        print("USAGE:")
        print("\tselect <-OPTION 1> <-OPTION 2> <FILENAME>")
        print("\nOPTIONS 1:")
        print("\t-csv : Specify CSV as the source of data. Data will be read and saved to a CSV file.")
        print("\t-db  : Specify Database as the source of data. Data will be read and saved to a SQLLite database.")
        print("\nOPTIONS 2:")
        print("\t-a : (Optional) Create the file if it doesn't exist.")
        print("\nFILENAME:")
        print("\tWhen select \"-csv\", FILENAME need to be provided. Otherwise a default file will be used.")
        print("\nEXAMPLES:")
        print("\t{:.<60}{:<30}".format("select -csv", "Specify CSV as the source of data."))
        print("\t{:.<60}{:<100}".format("select -csv -a files/data/employeeinfo.csv",
                                        "Specify a CSV file as the source of data. "
                                        "Create one if the path doesn't exist."))
        print("\t{:.<60}{:<30}".format("select -db", "Specify Database as the source of data."))

    @staticmethod
    def help_quit():
        print("USAGE:")
        print("\tquit <-OPTION>")
        print("\nOPTIONS:")
        print("\t-f : Force quitting the system without saving new data.")
        print("\nEXAMPLES:")
        print("\t{:.<20}{:<60}".format("quit", "Normal quit."))
        print("\t{:.<20}{:<60}".format("quit -f", "Force quitting the system without saving new data."))


# new_data = {'Male': 75.0, 'Female': 15.0}
# ViewConsole.plot_pie(new_data, "Gender")
# ViewConsole.plot_bar(new_data, "Gender")
