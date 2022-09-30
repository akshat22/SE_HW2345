from code.columns import Cols, Row
from code.util.Util import csv_fun, push, rnd, csv_fun2


class Data:
    """
    ‘Data‘ is a holder of ‘rows‘ and their summaries (in ‘cols‘).

    Parameters:
    src = location of the csv file to import from

    Attributes:
    rows = list of rows
    cols = summary of data
    """

    def __init__(self, src):
        self.cols = None
        self.rows = []

        if type(src) == str:
            # csv_fun(src, lambda row: self.add(row))
            csv_fun2(src, self.add, False)
        else:
            for row in enumerate(src or []):
                self.add(row)

    def add(self, xs):
        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row = push(self.rows, Row(xs))
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at])

    def stats(self, places, showCols, fun):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = []
        for col in showCols:
            v = fun(col)
            if type(v) is float:
                v = rnd(v, places)
            t[col.name] = v
        return t
