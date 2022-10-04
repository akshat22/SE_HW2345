import re
from code.columns.Num import Num
from code.columns.Sym import Sym


class Cols:

    """
    all     : a dictionary to store all variables
    X       : a dictionary to store all independent variables
    Y       : a dictionary to store all dependent variables
    klass   : a dictionary to store all the variables which are skipped
    """
    def __init__(self, names=None):
        if names is None:
            names = {}
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}
        number_x = 1
        number_y = 1

        for c in self.names:
            s = self.names[c]
            if bool(re.match("^[A-Z]{1}.*", s)):
                # print("Num", c,s)
                self.col = Num(c, s)
            else:
                # print("Sym", c,s)
                self.col = Sym(c, s)
            self.all[c] = self.col
            if not (re.search("[:$]", s)):
                if re.search("[!+-]", s):
                    self.y[number_y] = self.col
                    number_y += 1
                else:
                    self.x[number_x] = self.col
                    number_x += 1
            else:
                self.klass = self.col

        # for i in range(len(names)):
        #
        #     # Checking if it belongs to Num or Sym
        #     if re.search('^[A-Z]', self.names[i]):
        #         col = Num(i, self.names[i])
        #         self.all.append(col)
        #
        #         # Checking if the column needs to be skipped
        #         if not re.search(':$', self.names[i]):
        #             # Checking if the column is dependent or independent
        #             if re.search('[!+-]', self.names[i]):
        #                 self.y.append(col)
        #             else:
        #                 self.x.append(col)
        #     else:
        #         col = Sym(i, self.names[i])
        #         self.all.append(col)
        #
        #         # Checking if the column needs to be skipped
        #         if not re.search(':$', self.names[i]):
        #             # Checking if the column is dependent or independent
        #             if re.search('[!+-]', self.names[i]):
        #                 self.y.append(col)
        #             else:
        #                 self.x.append(col)
        #
        #     if re.search('[!$]', self.names[i]):
        #         self.klass = col
