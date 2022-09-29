import re
from code.columns.Num import Num
from code.columns.Sym import Sym


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for i in range(len(names)):

            # Checking if it belongs to Num or Sym
            if re.search('^[A-Z]', self.names[i]):
                col = Num(i, self.names[i])
                self.all.append(col)

                #Checking if the column needs to be skipped
                if not re.search(':$', self.names[i]):
                    #Checking if the column is dependent or independent
                    if re.search('[!+-]', self.names[i]):
                        self.y.append(col)
                    else:
                        self.x.append(col)
            else:
                col = Sym(i, self.names[i])
                self.all.append(col)

                #Checking if the column needs to be skipped
                if not re.search(':$', self.names[i]):
                    #Checking if the column is dependent or independent
                    if re.search('[!+-]', self.names[i]):
                        self.y.append(col)
                    else:
                        self.x.append(col)
            
            if re.search('[!$]', self.names[i]):
                self.klass = col