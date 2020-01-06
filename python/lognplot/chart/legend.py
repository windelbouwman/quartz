from enum import Enum

class LegendMode(Enum):
    SIGNAL_NAMES = 0
    CURSOR_VALUES = 1

class Legend:

    def __init__(self):
        self.modes = [LegendMode.SIGNAL_NAMES, LegendMode.CURSOR_VALUES]
        self.active_mode = 0

    def next_mode(self):
        self.active_mode = (self.active_mode + 1) % len(self.modes)

    @property
    def mode(self) -> LegendMode:
        return self.modes[self.active_mode] 