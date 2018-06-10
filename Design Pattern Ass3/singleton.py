class Data(object):
    """
    :Author: Vaishali Patel
    """
    EMPID = 0
    GENDER = 1
    AGE = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    BIRTHDAY = 6

    @property
    def count_data(self):
        pass
    @property
    def show_table(self):
        pass

    @property
    def show_chart(self):
        pass

if __name__ == '__main__':
    # Instantiate Object A
    objA = Data()

    # Instantiate Object B
    objB = Data()

    # Investigate the memory addresses of the two objects
    print (id(objA))
    print (id(objB))

    # Determine if they are the same instance
    if (id(objA) == id(objB)):
        print ("Same")
    else:
        print ("Different")

