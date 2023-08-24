
counter = 1
draw_count = 1
"""
class Plots:

    _a = 1

    def __init__(self):
        self._a = None
        self.reset_default_values()

    def reset_default_values(self):
        self._a = Plots._a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value


plot = Plots()
print(plot.a)

plot.a = 42
print(plot.a)

plot.reset_default_values()
print(plot.a)
"""
