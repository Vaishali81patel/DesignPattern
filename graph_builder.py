# written by Patel

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class GraphBuilder:
    _labels = []
    _sizes = []
    _plt = None

    def __init__(self, data):
        self._data = data

    def get_gender(self):
        self._labels = 'Male', 'Females'
        males = 0
        females = 0
        for row in self._data:
            if row[1] == 'M':
                males += 1
            else:
                females += 1
        self._sizes = [males, females]

    @abstractmethod
    def setup_gender_graph(self):
        pass

    def get_graph(self):
        return self._plt
