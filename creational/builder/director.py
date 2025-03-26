from builder import Builder

class Director:
    builder: Builder

    def __init__(self, builder):
        self.builder = builder

    def make(self, withServiceLine):
        self.builder.reset()
        self.builder.prepare()
        self.builder.mainWork()
        if withServiceLine:
            self.builder.addServiceLines()
        self.builder.finish()
