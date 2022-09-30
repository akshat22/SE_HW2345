# from util.Util import copy
import copy


class Row:
    def __init__(self, t):
        self.cells = t

        # Here, we have to replace copy.deepcopy with our own function 'copy' which is defined in Util.py
        cooked = copy.deepcopy(t)

        isEvaled = False
