from code.columns.Cols import *
from code.columns.Row import *
from code.util.Util import rnd, csvReader


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
        self.rows = {}

        if type(src) == str:
            # csv_fun(src, lambda row: self.add(row))
            csvReader(src, self.add)
        else:
            for row in src.values():
                self.add(row)

    def add(self, xs, row=None):
        if self.cols is None:
            self.cols = Cols(xs)
        else:
            row_r = Row(row)
            self.rows[1 + len(self.rows)] = row_r
            # row = push(self.rows, Row(xs))
            for todo in [self.cols.x.values(), self.cols.y.values()]:
                for col in todo:
                    col.add(row.cells[col.at])

    def stats(self, fun, places=2, showCols=None, dictionary=None):
        showCols = self.cols.x if not showCols else showCols
        dictionary = {}
        for key, value in showCols.items():
            if isinstance(value, Num):
                fun_to_call = Num.mid if fun == "mid" else Num.div
            else:
                fun_to_call = Sym.mid if fun == "mid" else Sym.div
            if len(value.numList) > 0:
                stat = fun_to_call(value)
                stat = rnd(stat, places) if isinstance(stat, float) else stat
                dictionary[value.name] = stat
        return dictionary