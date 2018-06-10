class MyClass(object):
#    __metaclass__ = Singleton

    attrib1 = 1
    attrib2 = 2

    def function1(self):
        pass

    def function2(self):
        pass

if __name__ == '__main__':
    # Instantiate Object A
    objA = MyClass()

    # Instantiate Object B
    objB = MyClass()

    # Investigate the memory addresses of the two objects
    print (id(objA))
    print (id(objB))

    # Determine if they are the same instance
    if (id(objA) == id(objB)):
        print ("Same")
    else:
        print ("Different")
