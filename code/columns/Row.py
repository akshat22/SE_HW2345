import copy


class Row:
    """
    `Row` holds one record
    """

    def __init__(self, row):
        self.cells = row
        self.cooked = copy.deepcopy(row)
        self.isEvaled = False
