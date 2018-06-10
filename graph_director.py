# written by Patel


class GraphDirector(object):
    def __init__(self, b):
        self.builder = b

    def set_builder(self, b):
        self.builder = b

    def construct(self):
        self.builder.get_gender()
        self.builder.setup_gender_graph()
        return self.builder.get_graph()
