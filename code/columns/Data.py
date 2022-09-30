from code.columns import Cols, Row
from code.util.Util import csv_fun, push, rnd

class Data:
    def __init__(self, src):
        self.cols = None
        self.rows = []

        if(type(src) == str):
            csv_fun(src, lambda row: self.add(row))

        else:
            for row in src:
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
