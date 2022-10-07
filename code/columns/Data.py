from code.columns.Num import Num
from code.columns.Row import Row
from code.columns.Sym import Sym
from code.util.Util import *


class Data:
    """
     `Data` is a holder of `rows` and their summaries (in `cols`)
    """

    def __init__(self, src=None) -> None:
        self.cols = None
        self.rows = {}
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src.values():
                self.add(row)

    def add(self, xs, row=None):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            r = Row(row)
            self.rows[1 + len(self.rows)] = r
            for todo in list(self.cols.x.values()) + list(self.cols.y.values()):
                try:
                    to_add = r.cells[todo.at]
                    if to_add:
                        todo.add(to_add)
                except Exception as e:
                    pass

    def stats(self, fun, places=2, showColumns=None, t=None):
        showColumns = self.cols.x if not showColumns else showColumns
        t = {}
        for key, value in showColumns.items():
            if isinstance(value, Num):
                fun_to_call = Num.mid if fun == "mid" else Num.div
            else:
                fun_to_call = Sym.mid if fun == "mid" else Sym.div
            if len(value.numList) > 0:
                stat = fun_to_call
                stat = rnd(stat, places) if isinstance(stat, float) else stat
                t[value.name] = stat
        return t

