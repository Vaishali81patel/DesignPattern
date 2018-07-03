# written by Patel


class GraphDirector(object):
    """
        Construct an object using the Builder interface.
        """

    def __init__(self, b):
        self.builder = b

    def set_builder(self, b):
        self.builder = b

    def construct(self):
        self._builder._show_pie(self, line)
        self._builder._show_bar(self, line)
        self._builder._show_scatter(self, line)
        return self.builder.get_graph()
