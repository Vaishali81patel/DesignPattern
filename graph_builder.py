# written by Patel

from abc import abstractmethod, ABCMeta

from six import add_metaclass

@add_metaclass(ABCMeta)
class GraphBuilder:
    _lebels = []
    _values = []
    _plt = None

    def __init__(self):
        self.graph = Graph()

    @abstractmethod
    def show_pie(self, line):
        pass

    @abstractmethod
    def show_bar(self, line):
        pass

    @abstractmethod
    def show_scatter(self, line):
        pass

    @abstractmethod
    def plot_pie(data, title=""):
        pass

    @abstractmethod
    def plot_bar(data, title=""):
        pass

    @abstractmethod
    def plot_scatter(data, title=""):
        pass

    def get_graph(self):
        return self._plt

